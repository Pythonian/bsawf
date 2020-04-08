from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    email = EmailField("What's your e-mail address?",
                       [DataRequired(), Length(3, 254), Email()])
    message = TextAreaField("What's your question or issue?",
                            [DataRequired(), Length(1, 8192)])
