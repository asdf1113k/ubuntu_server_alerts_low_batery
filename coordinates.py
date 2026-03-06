import requests as rq

responce_ipinfo = rq.get("https://ipinfo.io")

json_ipinfo = responce_ipinfo.json()

for key in json_ipinfo:
    print(key, ":", json_ipinfo[key])
