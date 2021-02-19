from app import app
from flask import render_template, request, url_for, redirect, flash

ans_dict = {}

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Write My Rights')


@app.route('/letterType')
def write_my_rights_info():
    return render_template("/letterType.html", title="Write My Rights Letter Type")


@app.route('/questions/questionOne')
def question1():
    return render_template("/questions/questionOne.html", title="Question One")


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    error = ''
    print('AAHHHHHHHHHHHHHHHHHHHHHH')
    try:
        print('UGHHHHHHHHHHHHHHHHHH')
        print(request.method)
        if request.method == 'POST':

            key = request.form['key']
            attempted_value = request.form['answer']
            next_page = request.form['next_page']
            # '#trying with json instead of form'
            # key = request.json['key']
            # attempted_value = request.json['value']
            # next_page = request.json['next_page']

            if type(attempted_value) == str:
                ans_dict[key] = attempted_value
                print(ans_dict)
                return redirect(next_page)
            else:
                error = "Invalid answer provided for name. Try Again"

        #return render_template("this_question", error = error)
        return error, 401
    except Exception as e:
        print(e)
        #return render_template("this_question", error = error)
        return 402
