from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Write My Rights')


@app.route('/letterType')
def write_my_rights_info():
    return render_template("/letterType.html", title="Write My Rights Letter Type")


@app.route('/question1')
def question_1():
    return render_template("/questions/questionOne.html", title="Question 1")
