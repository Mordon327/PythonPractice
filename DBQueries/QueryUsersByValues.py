import os
from flask import Flask, render_template, redirect, url_for, send_from_directory, g
import sqlite3
app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'databases/pythonPracticeDB')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

db = 1
print(db)