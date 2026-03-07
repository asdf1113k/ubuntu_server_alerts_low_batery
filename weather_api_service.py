from coordinates import json_ipinfo
import requests as rq
from my_token import TOKEN
# https://api.openweathermap.org/data/2.5/weather?lat=55.7&lon=37.5&appid=7549b3ff11a7b2f3cd25b56d21c83c6a&lang=ru&units=metric
loc = json_ipinfo["loc"].strip(",")
responce_api_openweather = rq.get(f"https://api.openweathermap.org/data/2.5/weather?lat={loc[0]}&lon={loc[1]}&appid={TOKEN}&lang=ru&units=metric")
json_openweather = responce_api_openweather.json()

if __name__ == "__main__":
    print(responce_api_openweather.status_code)
    json_openweathermap = responce_api_openweather.json()
    for key in json_openweathermap:
        print(key, ":", json_openweathermap[key])