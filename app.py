from flask import Flask, redirect, render_template, request

app = Flask(__name__)

responses =[]


QUESTIONS = {
    1: "Have you shopped here before?",
    2: "Did someone else shop with you today?",
    3: "On average, how much do you spend a month on frisbees?",
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
        responses.append(response)

    # Check if there is a next question
    next_qid = qid + 1
    if next_qid in QUESTIONS:
        question_text = QUESTIONS.get(next_qid)
        return render_template("questions.html", qid=next_qid, question_text=question_text)
    else:
        return redirect('/complete')


@app.route('/complete')
def complete():
    return render_template("complete.html", qid=4)



# @app.route('/question_1')
# def question_1():
#     return render_template("question_1.html")

# @app.route('/question_2')
# def question_2():
#     return render_template("question_2.html")

# @app.route('/question_3')
# def question_3():
#     return render_template("question_3.html")

# @app.route('/question_4')
# def question_4():
#     return render_template("question_4.html")

# @app.route('/complete')
# def complete():
#     return render_template("complete.html")
