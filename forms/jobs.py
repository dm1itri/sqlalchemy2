from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    team_leader_id = IntegerField("Team Leader id", validators=[DataRequired()])
    work_size = IntegerField("Work size", validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    category = IntegerField('Category', validators=[DataRequired()])
    submit = SubmitField('Submit')
