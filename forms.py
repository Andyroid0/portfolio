#! python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SendEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    email2 = StringField('Email', validators=[DataRequired(), Email(), EqualTo('email')])

    textBody = TextAreaField('Message', validators=[DataRequired(), Length(min=2, max=300)])

    submit = SubmitField('Send')

