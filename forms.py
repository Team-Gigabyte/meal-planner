from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import SelectMultipleField, StringField, PasswordField, SubmitField


class RegistrationForm(FlaskForm):
    diets = [
        "Vegetarian",
        "Vegan",
        "Keto Friendly",
        "Kosher",
        "Pescatarian",
        "Paleo",
        "Low Sugar",
        "Low Potassium",
        "Low Fat Abs",
        "Kidney Friendly",
        "Sugar Conscious",
        "Immuno Supportive",
    ]
    dietary_restrictions = [
        "Alcohol-Free",
        "Celery-Free",
        "Crustacean-Free",
        "Dairy-Free",
        "Egg-Free",
        "Fish-Free",
        "Fodmap-Free",
        "Gluten-Free",
        "Lupine-Free",
        "Mollusk-Free",
        "Mustard-Free",
        "No Oil Added",
        "Peanut-Free",
        "Pork-Free",
        "Red Meat Free",
        "Sesame-Free",
        "Shellfish-Free",
        "Soy-Free",
        "Sulfite-Free",
        "Tree Nut Free",
        "Wheat-Free",
    ]
    # username = StringField('Username', validators=[DataRequired()])
    # password = PasswordField('Password',validators=[DataRequired()])
    # password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    diet_checkboxes = SelectMultipleField("Special Diets", choices=diets)
    restriction_checkboxes = SelectMultipleField(
        "Excluded Ingredients", choices=dietary_restrictions
    )

    submit = SubmitField("Generate meal plan →")


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")
