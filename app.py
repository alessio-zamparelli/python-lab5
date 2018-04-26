
import db_operator as myDB
from flask import Flask, redirect, url_for, render_template, session, request

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
    username = session.get('username', '')
    if username != '':
        return render_template(url_for('taskList'))
    else:
        return render_template("index.html")

@app.route('/tasklist', methods=['POST'])
def taskList():
    username = session.get('username', '')
    if username=='':
        username = request.form['username']
        session['username'] = username
    tasks = myDB.showTasks(username)
    return render_template("tasklist.html", tasks=tasks)


@app.route('/logout')
def logout():
    del (session['username'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
