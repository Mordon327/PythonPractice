from flask import Flask, render_template, redirect, url_for
#When naming this file to app or wsgi, the command to run will be: flask run
#Otherwise it will be flask --app filename run
app = Flask(__name__)

@app.route("/hello")
def hello_world():
	return "<p>Hello, World!</p>"
	#flask --app hello run

@app.route("/")
def main_page():
	return render_template('mainPage.html')