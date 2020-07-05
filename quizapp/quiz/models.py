from quizapp import db

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question = db.Column(db.String(200),nullable=False)
    answers = db.relationship("Answer",backref='author',lazy=True)

class Answer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    answer = db.Column(db.String(20),nullable=False)
    isCorrect = db.Column(db.Boolean,default=False)
    questions = db.Column(db.Integer, db.ForeignKey('question.id'),nullable=False)


