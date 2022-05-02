from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Описание', validators=[DataRequired()])
    chief = IntegerField("Глава", validators=[DataRequired()])
    members = StringField("Сотрудники", validators=[DataRequired()])
    email = StringField('Email департамента', validators=[DataRequired()])
    submit = SubmitField('Отправить')
