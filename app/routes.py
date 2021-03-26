import urllib.parse
import stripe
import os
from os import path, environ
from app import app
from flask import render_template, request, redirect, make_response, jsonify
from app.emailer import Email
from app.worder import WordDoc
from app import letter_script
from dotenv import load_dotenv
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.flaskenv'))

stripe_keys = {
    "secret_key": environ.get("STRIPE_SECRET_KEY"),
    "publishable_key": environ.get("STRIPE_PUBLISHABLE_KEY"),
}

stripe.api_key = stripe_keys["secret_key"]


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

@app.route('/paymentOption')
def paymentOption():
    return render_template("/paymentOption.html", title="Payment Option")


@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)


@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://localhost:5000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "paymentDone",
            cancel_url=domain_url + "paymentOption",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": "EmploymentLetter",
                    "quantity": 1,
                    "currency": "cad",
                    "amount": "5000",
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403



@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        # TODO: run some custom code here

    return "Success", 200


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
            # else:
                # attempted_value = dict()
                # # if name for input = answer(1 - 10) this will store it all within a json object string before setting as a cookie
                # for i in range(9):
                #     if 'answer' + str(1 + i) not in request.form:
                #         break
                #     else:
                #         print(request.form['answer' + str(1+i)])
                #         attempted_value['a' + str(1+i)] = request.form['answer' + str(1+i)]
                # attempted_value = json.dumps(attempted_value)

            next_page = request.form['next_page']
            res = make_response(redirect('/questions' + next_page))

            if type(attempted_value) == str or type(attempted_value) == dict:
                if key == 'bossName':
                    if attempted_value == '':
                        attempted_value = 'Sir or Madam'
                res.set_cookie(key, attempted_value)
                return res
            else:
                error = "Invalid Answer"

        return error, 401
    except Exception as e:
        print(e)
        return error, 402


def month_delta(start_date, end_date):
    delta = relativedelta(end_date, start_date)
    return 12 * delta.years + delta.months


@app.route('/questions/getAnswers')
def getAnswers():
    ans = {}
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
    # vacation pay
    ans['vacation'] = request.cookies.get('vacation')
    # client's mood (determines the letter template)
    ans['mood'] = request.cookies.get('mood')

    # time worked at the company
    date_hired = datetime.strptime(request.cookies.get('hire_date'), '%Y-%m-%d')
    date_fired = datetime.strptime(request.cookies.get('fireDate'), '%Y-%m-%d')
    total_months_worked = (month_delta(date_hired, date_fired))
    ans['years_worked'] = int(total_months_worked/12)
    ans['months_worked'] = int((total_months_worked/12 % 1) * 12)

    # today's date
    ans['date'] = datetime.today().strftime("%B %d, %Y")
    # job start date
    ans['job_start_date'] = date_hired.strftime("%B %d, %Y")
    # Date of layoff
    ans['fire_date'] = date_fired.strftime("%B %d, %Y")
    # response date
    ans['response_date'] = datetime.strptime(request.cookies.get('deadline'), '%Y-%m-%d').strftime("%B %d, %Y")

    letter = letter_script.create_employment_letter_preview(ans)
    WordDoc(letter, ans).create()
    #Email(ans['email'], ans['name'] + ".docx").send()
    res = make_response(redirect('/questions/letterPreview'))
    letter = urllib.parse.quote(letter)
    res.set_cookie('written_letter', letter)

    return res