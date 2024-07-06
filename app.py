import os
from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
from forms import RegistrationForm, SignInForm
from get_recipes import get_recipes
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "gig-trade-secrets"
app_name = "GiG Meals"


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html", no_padding=True, title="Home", app_name=app_name
    )


@app.route("/onboarding", methods=["GET", "POST"])
def onboarding():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("form validated")
        diets = form.diet_checkboxes.data
        restrictions = form.restriction_checkboxes.data
        return redirect(
            url_for("currentmealplan", diets=diets, restrictions=restrictions)
        )
    return render_template(
        "onboarding.html", title="Get Started", form=form, app_name=app_name
    )


@app.route("/currentmealplan")
def currentmealplan():
    diets = request.args.getlist("diets")
    restrictions = request.args.getlist("restrictions")
    recipes = get_recipes(diets, restrictions)
    return render_template(
        "currentmealplan.html",
        title="Your Meal Plan",
        app_name=app_name,
        recipes=recipes,
    )
