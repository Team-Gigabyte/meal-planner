from typing import NotRequired
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import SelectMultipleField, StringField, PasswordField, SubmitField

class RegistrationForm(FlaskForm): 
    diets = ['Vegetarian', 'Vegan', 'Keto', 'Paleo', 'Gluten-Free', 'Dairy-Free', 'Low-Carb', 'Low-Fat', 'Low-Sodium', 'Mediterranean', 'Whole30', 'Pescatarian', 'Flexitarian']
    dietary_restrictions = ['Peanuts', 'Tree Nuts', 'Soy', 'Dairy', 'Eggs', 'Wheat', 'Fish', 'Shellfish', 'Other']
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    diet_checkboxes = SelectMultipleField('Special Diets', choices=diets)
    restriction_checkboxes = SelectMultipleField('Dietary Restrictions', choices=dietary_restrictions)

    submit = SubmitField('Register')
    
class SignInForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign In')