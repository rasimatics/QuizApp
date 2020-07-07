from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignUpForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField('Email', validators=[
                        DataRequired(), Length(min=5, max=40), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6, max=20), EqualTo('password',
                                                                                                   message="Passwords must match")
                                                    ])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Length(min=5, max=40), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
