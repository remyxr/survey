from flask import Flask, redirect, render_template, request, session
import pdb

app = Flask(__name__)
app.secret_key="aaaa"
responses =[]


QUESTIONS = {
    1: "Have you shopped here before?",
    2: "Did someone else shop with you today?",
    3: "On average, do you spend more than $10,000 a month on frisbees?",
    4: "Are you likely to shop here again?"
}


@app.route('/')
def home():
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/questions')
def show_questions():
    qid = 1 
    question_text = QUESTIONS.get(qid)
    if question_text is not None:
        return render_template("questions.html", qid=qid, question_text=question_text)
    else:
        return "Question not found"

@app.route('/question/<int:qid>', methods=['GET', 'POST'])
def question(qid):
    if request.method == 'POST':
        response = request.form.get('response')
        responses = session.get('responses', [])
        responses.append(response)
        session['responses'] = responses

    # Check if there is a next question
    next_qid = qid + 1
    if next_qid in QUESTIONS:
        question_text = QUESTIONS.get(next_qid)
        return render_template("questions.html", qid=next_qid, question_text=question_text)
    else:
        return redirect('/complete')
    
@app.route('/complete')
def complete():
    return render_template("complete.html", qid=3, responses=session['responses'])
