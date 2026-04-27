import os
from flask import Flask, render_template, redirect, url_for, send_from_directory
#When naming this file to app or wsgi, the command to run will be: flask run
#Otherwise it will be flask --app filename run

app = Flask(__name__)
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
def signin_page():
	return render_template('signInPage.html')