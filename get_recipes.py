import requests
import os


def get_recipes(diets, restrictions):  # using edamam recipe search API
    endpoint = "https://api.edamam.com/api/recipes/v2"
    app_id = os.environ.get("EDAMAM_APP_ID")
    app_key = os.environ.get("EDAMAM_APP_KEY")
    # query = f"?type=public&diet={diets}&app_id={app_id}&app_key={app_key}"
    # build query programmatically
    query = f"?type=public&app_id={app_id}&app_key={app_key}"
    for diet in diets:
        query += f"&health={diet.lower().replace(' ', '-')}"
    for restriction in restrictions:
        query += f"&health={restriction.lower().replace(' ', '-')}-free"
    print(endpoint + query)
    response = requests.get(endpoint + query)
    print(response)
    return response
