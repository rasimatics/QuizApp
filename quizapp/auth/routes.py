from flask import Blueprint,render_template,request,redirect,url_for,session
from quizapp import db
from .models import User

auth = Blueprint('auth',__name__,url_prefix='/auth')


@auth.route('/',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('quiz.index'))
    return render_template('auth/register.html')

