from app import app
from flask import render_template, request, redirect, make_response

ans_dict = {}

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Write My Rights')


@app.route('/letterType')
def write_my_rights_info():
    return render_template("/letterType.html", title="Write My Rights Letter Type")


@app.route('/questions/<question>')
def question(question):
    return render_template("questions/"+question+".html", title=question)

@app.route('/questions/fetchLetter')
def fetchLetter():
    return render_template("/questions/fetchLetter.html", title="fetchLetter")

@app.route('/paymentDone')
def paymentDone():
    return render_template("/paymentDone.html", title="Payment Done")


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    error = ''
    try:
        if request.method == 'POST':

            key = request.form['key']
            attempted_value = request.form['answer']
            next_page = request.form['next_page']
            res = make_response(redirect('/questions' + next_page))

            if type(attempted_value) == str:
                res.set_cookie(key, attempted_value)
                return res
            else:
                error = "Invalid answer provided for name. Try Again"

        #return render_template("this_question", error = error)
        return error, 401
    except Exception as e:
        print(e)
        #return render_template("this_question", error = error)
        return 402


@app.route('/getAnswers')
def getAnswers():
    ans = {}
    ans['name'] = request.cookies.get('name')
    ans['company'] = request.cookies.get('company')
    ans['boss_name'] = request.cookies.get('bossName')
    ans['length'] = request.cookies.get('length')
    ans['reason'] = request.cookies.get('reason')
    ans['severance'] = request.cookies.get('severance')
    ans['email'] = request.cookies.get('email')
    ans['mood'] = request.cookies.get('mood')
    return ans