from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    team_leader_id = IntegerField("Ответственный", validators=[DataRequired()])
    work_size = IntegerField("Объем работы", validators=[DataRequired()])
    collaborators = StringField('Помощники', validators=[DataRequired()])
    category = IntegerField('Категория', validators=[DataRequired()])
    is_finished = BooleanField('Выполнена')
    submit = SubmitField('Отправить')
