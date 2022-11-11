from sql_base.dbmanager import UserManager


def get_user(user_id: int) -> str:
    return UserManager(user_id, path='sql_base/touragency.db', scripts_path='sql_base/scripts/').get()
