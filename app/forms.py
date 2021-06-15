from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField , TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo 

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit  = SubmitField('Login')

class CreatePost(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Share Post')
