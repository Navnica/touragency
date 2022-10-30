import sqlite3
import os


class DbWorker:
	def __init__(self, db_name, db_dir) -> None:
		self.db_name = db_name
		self.db_dir = db_dir
		self.db_scripts = ('script.sql', 'fill.sql')
		self.db_connect = None
		self.db_cursor = None

	def scripts_exists(self) -> bool:
		exists = True

		for script in self.db_scripts:
			if not os.path.exists(f'{self.db_dir}/sqlscripts/{script}'):
				exists = False
				break

		return exists

	def db_exists(self) -> bool:
		return os.path.exists(f'{self.db_dir}/{self.db_name}')

	def execute_scripts(self):
		if not self.scripts_exists():
			return 'err1'

		if not self.db_connect:
			self.create_db() 

		for script in self.db_scripts:
			self.db_cursor.executescript(open(f'{self.db_dir}/sqlscripts/{script}').read())

	def create_db(self) -> None:
		self.db_connect = sqlite3.connect(f'{self.db_dir}/{self.db_name}')
		self.db_cursor = self.db_connect.cursor()

		if self.execute_scripts() == 'err1':
			print('Are one or more scripts missing')
			return None

		self.db_connect.commit()


		
