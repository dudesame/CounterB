from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField('Text file', validators=[FileRequired(), FileAllowed(['txt'], 'TXT Files only')])
    submit = SubmitField('ПЕРЕДАТЬ')
