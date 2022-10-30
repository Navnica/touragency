from dbworker import DbWorker


if __name__ == '__main__':
	db_worker = DbWorker(db_dir='../', db_name='touragency.db')

	if not db_worker.db_exists():
		db_worker.create_db()
