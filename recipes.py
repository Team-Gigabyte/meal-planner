import requests
import os


def get_recipes(diets, restrictions, mealType = 'Lunch'):  # using edamam recipe search API
    endpoint = "https://api.edamam.com/api/recipes/v2"
    app_id = os.environ.get("EDAMAM_APP_ID")
    app_key = os.environ.get("EDAMAM_APP_KEY")
    query = f"?type=public&app_id={app_id}&app_key={app_key}&mealType={mealType}"
    for diet in diets:
        query += f"&health={diet.lower().replace(' ', '-')}"
    for restriction in restrictions:
        query += f"&health={restriction.lower().replace(' ', '-')}-free"
    print(endpoint + query)
    response = requests.get(endpoint + query)
    recipes = response.json()
    print(recipes.keys())
    recipes = recipes['hits']
    return recipes

def build_weekly_meal_plan(diets, restrictions):
    plan = []
    for day in range(7):
        day_recipes = {}
        for meal in ['Breakfast', 'Lunch', 'Dinner']:
            day_recipes[meal] = get_recipes(diets, restrictions, meal)[0]
        plan.append(day_recipes)
    print(plan)
    return plan
    