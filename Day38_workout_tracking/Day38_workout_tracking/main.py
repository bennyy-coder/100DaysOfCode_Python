import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "79"
HEIGHT_CM = "176"
AGE = "29"

NUTRITION_ID = "113802a"
NUTRITION_APIKEY = "d34157c8347863c4e18ca9dd9a"
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_ENDPOINT = "https://api.sheety.co/4946e00f714c07fd3e8ed1933e80/workoutTracking/workouts"

headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_APIKEY,
}

exercise_text = input("Tell me which exercises you did:")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITION_ENDPOINT, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer asdfuyi124nkjl128906sxf"
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)