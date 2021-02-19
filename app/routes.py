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


# @app.route('/question1')
# def question_1():
#     return render_template("/questions/questionOne.html", title="Question 1")

@app.route('/answer', methods=['GET', 'POST'])
def process_answer():
    error = ''
    try:
        if request.method == 'POST':
            key = request.form['key']
            attempted_value = request.form['value']

            if type(attempted_value) == str:
                ans_dict[key] = attempted_value
                print(ans_dict)
                #return redirect(url_for('next_question'))
                return "data stored", 201
            else:
                error = "Invalid answer provided for name. Try Again"

        #return render_template("this_question", error = error)
        return error, 400

    except Exception as e:
        pass
        #return render_template("this_question", error = error)
        return error, 400
