from flask import Flask, render_template, request, redirect
import spacy
from textblob import TextBlob
from transformers import pipeline
from db import Database

app = Flask(__name__)

# Load models
nlp = spacy.load("en_core_web_sm")
abuse_classifier = pipeline('text-classification', model='unitary/toxic-bert')

dbo = Database()

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message="Email already exists")

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)
    if response:
        return redirect("/profile")
    else:
        return render_template('login.html', message="Incorrect email / password")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    text = request.form.get('ner_text')
    response = ner(text)
    return render_template('NER.html', response=response)

def ner(text):
    doc = nlp(text)
    entities = [{'name': ent.text, 'category': ent.label_} for ent in doc.ents]
    return {'entities': entities}

@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    blob = TextBlob(text)
    sentiment = blob.sentiment
    response = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    return render_template('sentiment.html', response=response)

@app.route('/perform_abuse_detection', methods=['POST'])
def perform_abuse_detection():
    text = request.form.get('abuse_text')
    result = abuse_classifier(text)
    return render_template('abuse_detection.html', response=result)

@app.route("/ner")
def ner_form():
    return render_template("ner.html")

@app.route("/sentiment")
def sentiment_form():
    return render_template("sentiment.html")

@app.route("/abuse_detection")
def abuse_detection_form():
    return render_template("abuse_detection.html")

if __name__ == "__main__":
    app.run(debug=True)
