import os
from flask import Flask, render_template, redirect, url_for, send_from_directory, g, jsonify, request
from datetime import datetime
import sqlite3
#When naming this file to app or wsgi, the command to run will be: flask run
#Otherwise it will be flask --app filename run



app = Flask(__name__)


def connect_db():
	sql = sqlite3.connect(os.path.join(app.root_path, 'databases/pythonPracticeDB'))
	sql.row_factory = sqlite3.Row
	return sql

def get_db():
	if not hasattr(g, 'sqlite3'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

#Prevent memory leak by closing the connection
@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

@app.route("/")
def main_page():
	return render_template('mainPage.html')

@app.route("/contact")
def contact():
	return render_template('contactMePage.html')

@app.route("/about")
def about_page():
	return render_template('aboutPage.html')

@app.route("/signin")
def viewusers():
	db = get_db()
	cursor = db.execute('SELECT * FROM Users')
	results = cursor.fetchall()
	#return render_template('signInPage.html')
	return render_template('signInPage.html', results = results)

#Simple API call
@app.route('/users', methods=['POST'])
def create_user():
	db = get_db()
	FIRST_NAME = request.json['FIRST_NAME']
	LAST_NAME = request.json['LAST_NAME']
	CREATE_DATE = datetime.now()
	EMAIL_ADDRESS = request.json['EMAIL_ADDRESS']
	#Execute sql on the db connection. Format Insert Into table (columns), Values (question marks used as placeholders), [replacement values for question marks]
	db.execute('INSERT INTO Users (FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, CREATE_DATE, IS_ADMIN) VALUES (?, ?, ?, ?, ?)', [FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, CREATE_DATE, False])
	db.commit()
	return jsonify({'message': 'User created successfully!'})

#Read
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	db = get_db()
	cursor = db.execute('SELECT * FROM users WHERE ID = ?', [user_id])
	result = cursor.fetchone()
	if not result:
		return jsonify({'error': 'User not found'})
	return f"<h1>The Id is {result['ID']}.<br> The Name is {result['FIRST_NAME']} {result['LAST_NAME']}"

#Update
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
	db = get_db()
	firstName = request.json['firstName']
	lastName = request.json['lastName']
	db.execute('UPDATE Users SET FIRST_NAME = ?, LAST_NAME = ? WHERE ID = ?', [firstName, lastName, user_id])
	db.commit()
	return jsonify({'message': "User updated successfully!"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	db = get_db()
	db.execute('DELETE FROM Users WHERE ID = ?', [user_id])
	db.commit()
	return jsonify({'message': 'User was deleted successfully!'})