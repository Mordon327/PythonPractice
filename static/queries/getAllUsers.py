class getAllUsersList(dbConnection):
	db = dbConnection
	cursor = db.execute('SELECT * FROM users WHERE 1')
	return cursor.fetchone()