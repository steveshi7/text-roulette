from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class TextInputForm(Form):
    text = StringField('text', validators=[DataRequired()])
