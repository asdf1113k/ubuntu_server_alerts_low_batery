import requests as rq

headers = {
    "list-type": "application/json"
}

responce_open_meteo = rq.get("https://forecastapi.com/v2/forecast", headers=headers)

json_open_meteo = responce_open_meteo.json()

for key in json_open_meteo:
    print(key, ":", json_open_meteo[key])

