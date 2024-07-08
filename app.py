import os
from flask import Flask, redirect, render_template, url_for, session
from datetime import datetime
from forms import RegistrationForm, SignInForm
import recipes
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

try:
    from dotenv import load_dotenv

    load_dotenv()
except:
    pass


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
        # diets = form.diet_checkboxes.data
        # restrictions = form.restriction_checkboxes.data
        session["diets"] = form.diet_checkboxes.data
        print(type(session["diets"]))
        session["restrictions"] = form.restriction_checkboxes.data
        return redirect(url_for("currentmealplan"))
    return render_template(
        "onboarding.html", title="Get Started", form=form, app_name=app_name
    )


@app.route("/currentmealplan")
def currentmealplan():
    print("returning current meal plan")
    # diets = request.args.getlist("diets")
    # restrictions = request.args.getlist("restrictions")
    if (not "diets" in session) or (not "restrictions" in session):
        return redirect(url_for("onboarding"))

    plan = recipes.build_weekly_meal_plan(session["diets"], session["restrictions"])

    return render_template(
        "currentmealplan.html",
        title="Your Meal Plan",
        app_name=app_name,
        meal_plan=plan,
    )
