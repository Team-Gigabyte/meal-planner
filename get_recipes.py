import requests
import os


def get_recipes(diets, restrictions):  # using edamam recipe search API
    endpoint = "https://api.edamam.com/api/recipes/v2"
    app_id = os.environ.get("EDAMAM_APP_ID")
    app_key = os.environ.get("EDAMAM_APP_KEY")
    query = f"?type=public&diet={diets}&app_id={app_id}&app_key={app_key}"
    print(diets, restrictions)
