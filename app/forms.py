from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    name = StringField('Name', validators = [InputRequired()])
    phone_number = StringField('Phone Number', validators = [InputRequired(), Length(min = 7, max = 14)])
    address = StringField('Address', validators = [InputRequired()])
    submit = SubmitField()

    # def clean_phone_number(self):
    #     output = ''
    #     for digit in self.phone_number.data:
    #         if digit.isdigit():
    #             output += digit