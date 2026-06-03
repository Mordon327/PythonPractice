from datetime import datetime
current_moment = datetime.now()
def update_user(user_id):
	db = get_db()
	firstName = request.json['firstName']
	lastName = request.json['lastName']
	emailAddress = request.json['emailAddress']
	password = request.json['password']
	db.execute(
		'INSERT INTO Users (FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PASSWORD, CREATE_DATE, PASSWORD_CREATE_DATE, IS_ADMIN) VALUES (?, ?, ?, ?, ?, ?, ?)',
		[firstName, lastName, emailAddress, password, current_moment, current_moment, 0]
	)
	db.commit()