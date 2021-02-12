from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Write My Rights')


@app.route('/writemyrights')
def write_my_rights_info():
    return render_template("/writemyrights.html", title="Write My Rights Info")
