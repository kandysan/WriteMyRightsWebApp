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

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.flaskenv'))

ans_dict = {}

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
    return render_template("/paymentOption2.html", title="Payment Option")


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

