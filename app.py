
import db_operator as myDB
from flask import Flask, redirect, url_for, render_template, session

import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

app = Flask(__name__)
app.secret_key = "veryveryveryfucsdakjkkingseckjsbtydfdcretkey"



@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    tasks = myDB.showTasks()
    return render_template("index.html", tasks=tasks)


if __name__ == '__main__':
    app.run()
