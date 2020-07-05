from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hello world'
db = SQLAlchemy(app)

from quizapp.auth.routes import auth
from quizapp.quiz.routes import quiz

app.register_blueprint(auth)
app.register_blueprint(quiz)
