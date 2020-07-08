from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from quizapp import db
from .models import User
from .forms import LoginForm, SignUpForm
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup', methods=['POST', 'GET'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=request.form['username'],email=request.form['email'], password=generate_password_hash(
            request.form['password'], method='sha256'))
        db.session.add(user)
        db.session.commit()
        flash("You registered succesfully! Now you can login")
        return redirect('/auth/login')
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if not user and not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        login_user(user)
        flash("You loged in succesfully")
        return redirect(url_for('quiz.questions'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('quiz.questions'))

@auth.route('/users')
@auth.route('/users/<int:page>')
@login_required
def users(page=1):
    users = User.query.paginate(page,1,False)
    return render_template('auth/users.html',users=users)

