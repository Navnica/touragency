import sqlite3
import os
import sql_base.errors as errors
import json


class DbManager:
    def __init__(self, path: str = 'touragency.db', scripts_path: str = './scripts'):
        self.path = path
        self.script_path = scripts_path
        self.scripts = []
        self.add_sql_scripts('create.sql', 'fill.sql')
        self.connect = None
        self.cursor = None
        self.create_db()

    def add_sql_scripts(self, *scripts: str) -> None:
        [self.scripts.append(script) for script in scripts]

    def check_sql_scripts(self) -> bool:
        for script in self.scripts:
            if not os.path.exists(f'{self.script_path}{"/" if self.script_path[-1] != "/" else ""}{script}'):
                raise errors.MissedScript

        return True

    def check_db(self) -> bool:
        return os.path.exists(self.path)

    def create_db(self) -> None:
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()

        if not self.check_sql_scripts():
            raise errors.MissedScript

        self.connect.commit()

    def execute_sql_script(self, name: str) -> None:
        if name not in self.scripts:
            raise errors.UnregisteredScript

        if not self.check_db():
            raise errors.DatabaseNotExists

        self.cursor.executescript(open(f'{self.script_path}{"/" if self.script_path[-1] != "/" else ""}{name}').read())


class UserManager:
    def __init__(self, user_id: int, path: str = 'touragency.db', scripts_path: str = './scripts') -> None:
        self.user_id = user_id
        self.dbmanager = DbManager(path, scripts_path)

    def get(self) -> str:
        user = self.dbmanager.cursor.execute(f'select * from User where id=1').fetchall()
        if not user:
            return 'user : none'

        return json.dumps(user[0])
