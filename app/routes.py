import urllib.parse
from app import app
from flask import render_template, request, redirect, make_response
from app import letter_script
import json
import datetime

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
    date = datetime.date.today()
    date = date.strftime("%m/%d/%Y")
    d = datetime.timedelta()
    ans = {}
    # todays date
    ans['date'] = date
    # job start date
    ans['job_start_date'] = '2021-01-01'
    # response date
    ans['response_date'] = request.cookies.get('deadline')
    # client name
    ans['name'] = request.cookies.get('name')
    # client home address
    ans['personal_address'] = request.cookies.get('personalAddress')
    # client email
    ans['email'] = request.cookies.get('email')
    # company name
    ans['company_name'] = request.cookies.get('company')
    # company's address
    ans['company_address'] = request.cookies.get('employerAddress')
    # client job title
    ans['job_title'] = request.cookies.get('jobTitle')
    # length of time to find a job
    ans['findJobLength'] = request.cookies.get('findJobLength')
    # Amount of job experience
    ans['experience'] = request.cookies.get('experience')
    # company boss' name
    ans['boss_name'] = request.cookies.get('bossName')
    # reason for layoff
    ans['reason'] = request.cookies.get('reason')
    # severance paid (in weeks/months)
    ans['severance_paid'] = request.cookies.get('severance')
    # severance Demand
    ans['severance_demand'] = request.cookies.get('severanceDemand')
    # client's mood (determines the letter template)
    ans['mood'] = request.cookies.get('mood')
    # time worked at the company
    ans['time_worked']['years'] = json.loads(request.cookies.get('time_worked'))['a1']
    ans['time_worked']['months'] = json.loads(request.cookies.get('time_worked'))['a2']

    letter = letter_script.create_employment_letter(ans)
    res = make_response(redirect('/questions/letterPreview'))
    letter = urllib.parse.quote(letter)
    res.set_cookie('written_letter', letter)
    return res
