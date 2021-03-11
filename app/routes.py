import urllib.parse
from app import app
from flask import render_template, request, redirect, make_response
from app.emailer import Email
from app.worder import WordDoc
from app import letter_script
import json

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

            # single answers
            if 'answer' in request.form:
                attempted_value = request.form['answer']
            # multi answers up to 10
            elif 'answer1' in request.form:
                attempted_value = dict()
                for i in range(9):
                    if 'answer' + str(1 + i) not in request.form:
                        break
                    else:
                        print(request.form['answer' + str(1+i)])
                        attempted_value['a' + str(1+i)] = request.form['answer' + str(1+i)]
                attempted_value = json.dumps(attempted_value)

            next_page = request.form['next_page']
            res = make_response(redirect('/questions' + next_page))

            if type(attempted_value) == str or type(attempted_value) == dict:
                res.set_cookie(key, attempted_value)
                return res
            else:
                error = "Invalid answer provided for name. Try Again"

        #return render_template("this_question", error = error)
        return error, 401
    except Exception as e:
        print(e)
        #return render_template("this_question", error = error)
        return error, 402


@app.route('/questions/getAnswers')
def getAnswers():
    ans = {}
    ans['time_worked'] = {}
    ans['name'] = request.cookies.get('name')
    ans['company_name'] = request.cookies.get('company')
    ans['job_title'] = request.cookies.get('jobTitle')
    ans['experience'] = request.cookies.get('experience')
    ans['boss_name'] = request.cookies.get('bossName')
    ans['reason'] = request.cookies.get('reason')
    ans['severance'] = request.cookies.get('severance')
    ans['email'] = request.cookies.get('email')
    ans['mood'] = request.cookies.get('mood')
    ans['address'] = request.cookies.get('personalAddress')
    ans['company_address'] = request.cookies.get('employerAddress')
    ans['time_worked']['years'] = json.loads(request.cookies.get('time_worked'))['a1']
    ans['time_worked']['months'] = json.loads(request.cookies.get('time_worked'))['a2']
    letter = letter_script.create_employment_letter(ans)
    print(letter)
    WordDoc(letter, ans).create()
    #Email(ans['email'], ans['name'] + ".docx").send()
    res = make_response(redirect('/questions/letterPreview'))
    letter = urllib.parse.quote(letter)
    res.set_cookie('written_letter', letter)
    return res

