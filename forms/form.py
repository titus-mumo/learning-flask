from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

class ChessPieceForm(FlaskForm):
    name = StringField("Chess peice name", validators=[DataRequired()])
    points = IntegerField("Total points", validators=[DataRequired(), NumberRange(min=1, max=9, message="Pointts must be between 1 and 9")])
    submit = SubmitField('Add piece')


