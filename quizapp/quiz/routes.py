from flask import Blueprint, render_template, request, redirect, flash
from .models import Answer, Question
from quizapp import db
from flask_login import login_required


quiz = Blueprint('quiz', __name__, url_prefix='/quiz/')

@quiz.route('/', methods=['GET'])
@login_required
def questions():
    questions = Question.query.all()
    answers = Answer.query.all()
    return render_template('quiz/index.html', questions=questions, answers=answers)


@quiz.route('/', methods=['POST'])
@login_required
def check():
    if request.method == "POST":
        questions = list(dict(request.form))
        questionAndAnswers = []
        correct = 0
        for question in questions:
            object = {'questionId': int(
                question), 'answerId': int(request.form[question])}
            questionAndAnswers.append(object)
            if Answer.query.filter_by(questions=int(question), id=int(request.form[question])).first().isCorrect:
                correct += 1
        flash(f"You have {correct} correct answers", 'info')
        questions = Question.query.all()
        answers = Answer.query.all()
        return render_template('quiz/index.html', questions=questions, answers=answers, written=questionAndAnswers)
