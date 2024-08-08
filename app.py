import os
from flask import Flask, redirect, render_template, request, url_for, session
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
        session["fave_recipes"] = ["placeholder"]
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


@app.route("/add_to_favorites", methods=["POST"])
def add_to_favorites():
    try:
        uri = request.get_json()["uri"]
        print(uri)
        recipe_id = uri.split("recipe_")[1]
        if recipe_id not in session["fave_recipes"]:
            session["fave_recipes"] += [recipe_id]
        print(recipe_id, session["fave_recipes"])
        return recipe_id
    except Exception as e:
        print(e)
        return "Error adding recipe to favorites", 400

@app.route("/remove_from_favorites", methods=["POST"])
def remove_from_favorites():
    try:
        uri = request.get_json()["uri"]
        recipe_id = uri.split("recipe_")[1]
        print(recipe_id, session["fave_recipes"])
        if recipe_id in session["fave_recipes"]:
            arr = session["fave_recipes"]
            arr.remove(recipe_id)
            session["fave_recipes"] = arr
        else:
            print("Recipe not in favorites")
        print(recipe_id, session["fave_recipes"])
    
        return recipe_id
    except Exception as e: 
        print(e)
        return "Error removing recipe from favorites", 400

@app.route("/favorites")
def favorites():
    if not "fave_recipes" in session:
        return redirect(url_for("onboarding"))
    print(session["fave_recipes"])
    if len(session["fave_recipes"]) <= 1:
        return render_template(
            "favorites.html",
            title="Favorites",
            app_name=app_name,
            fave_meals=[],
        )
    meals = recipes.uris_to_recipes(session["fave_recipes"])
    return render_template(
        "favorites.html",
        title="Favorites",
        app_name=app_name,
        fave_meals=meals,
    )
