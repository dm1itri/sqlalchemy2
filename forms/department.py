from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    chief = IntegerField("Chief", validators=[DataRequired()])
    members = StringField("Members", validators=[DataRequired()])
    email = StringField('Department email', validators=[DataRequired()])
    submit = SubmitField('Submit')
