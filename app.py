from flask import Flask, request, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, Survey, surveys
app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'secret'
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    survey = surveys["satisfaction"]
    return render_template("home.html", instructions=survey.instructions)

@app.route('/questions/0')
def questions_page():
    return render_template('questions.html')

@app.route('/question/1', methods = ['GET','POST'])
def question1_page():
    survey = surveys["satisfaction"]
    if request.method == 'POST':
        response = request.form.get('response')
        responses.append(response)
        return redirect('/question/2')
    return render_template('question1.html', question=survey.questions[0])

@app.route('/question/2', methods =['GET', 'POST'])
def question2_page():
    survey = surveys["satisfaction"]
    if request.method == 'POST':
        response = request.form.get('response')
        responses.append(response)
        return redirect('/question/3')
    return render_template('question2.html', 
    question = survey.questions[1])

@app.route('/question/3', methods = ['GET', 'POST'])
def question3_page():
    survey = surveys["satisfaction"]
    if request.method == 'POST':
        response = request.form.get('response')
        responses.append(response)
        return redirect('/question/4')
    return render_template('question3.html', question = survey.questions[2])

@app.route('/question/4', methods = ['GET', 'POST'])
def question4_page():
    survey = surveys["satisfaction"]
    if request.method == 'POST':
        response = request.form.get('response')
        responses.append(response)
        return redirect('/thanks')
    return render_template('question4.html', question = survey.questions[3])

@app.route('/thanks')
def thanks_page():
    return render_template('thanks.html', responses=responses)

@app.route('/reset-survey', methods=['GET'])
def reset_survey_and_redirect():
    responses.clear()
    return redirect('/question/1')



app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False





