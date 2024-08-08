import requests
import os

endpoint = "https://api.edamam.com/api/recipes/v2"
app_id = os.environ.get("EDAMAM_APP_ID")
app_key = os.environ.get("EDAMAM_APP_KEY")


def get_recipes(
    diets, restrictions, mealType="Lunch"
):  # using edamam recipe search API
    query = f"?type=public&random=true&app_id={app_id}&app_key={app_key}&mealType={mealType}"
    for diet in diets:
        query += f"&health={diet.lower().replace(' ', '-')}"
    for restriction in restrictions:
        query += f"&health={restriction.lower().replace(' ', '-')}"
    query += "&glycemic-index=0-55"  # does this work?
    print(endpoint + query)
    response = requests.get(endpoint + query)
    recipes = response.json()
    print(recipes.keys())
    recipes = recipes["hits"]
    return recipes


def build_weekly_meal_plan(diets, restrictions):
    plan = []
    foundRecipes = {"Breakfast": [], "Lunch": [], "Dinner": []}
    for meal in ["Breakfast", "Lunch", "Dinner"]:
        foundRecipes[meal] = get_recipes(diets, restrictions, meal)
    for day in range(7):
        day_recipes = {}
        for meal in ["Breakfast", "Lunch", "Dinner"]:
            day_recipes[meal] = foundRecipes[meal][day]["recipe"]
        plan.append(day_recipes)
    # print(plan)
    print("Plan built")
    return plan


def uris_to_recipes(recipe_ids):
    query = f"?type=public&app_id={app_id}&app_key={app_key}"
    for recipe_id in recipe_ids:
        if recipe_id != "placeholder":
            query += f"&uri=http%3A%2F%2Fwww.edamam.com%2Fontologies%2Fedamam.owl%23recipe_{recipe_id}"
    print(endpoint + "/by-uri" + query)
    response = requests.get(endpoint + "/by-uri" + query)
    recipes = response.json()
    recipes = recipes["hits"]
    return recipes
