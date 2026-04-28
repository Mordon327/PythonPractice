import os
from flask import Flask, render_template, redirect, url_for, send_from_directory, g
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