import sqlite3
import os
import errors


class DbManager:
    def __init__(self, path, scripts_path):
        self.path = path
        self.script_path = scripts_path
        self.scripts = []
        self.add_sql_scripts('create.sql', 'fill.sql')
        self.connect = None
        self.cursor = None

    def add_sql_scripts(self, *scripts: str) -> None:
        [self.scripts.append(script) for script in scripts]

    def check_scripts(self) -> bool:
        for script in self.scripts:
            if not os.path.exists(f'{self.script_path}{"/" if self.script_path[-1] != "/" else ""}{script}'):
                raise errors.MissedScript

        return True

    def check_db(self) -> bool:
        return os.path.exists(self.path)

    def create_db(self) -> None:
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()

        if not self.check_scripts():
            return None

        self.connect.commit()

    def execute_sql_script(self, name: str) -> None:
        if name not in self.scripts:
            raise errors.UnregisteredScript

        if not self.check_db():
            raise errors.DatabaseNotExists

        self.cursor.executescript(open(f'{self.script_path}{"/" if self.script_path[-1] != "/" else ""}{name}').read())
