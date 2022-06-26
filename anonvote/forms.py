from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, InputRequired


class PollForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    description = StringField("Description")


class ItemForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
