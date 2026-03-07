import requests as rq

responce_ipinfo = rq.get("https://ipinfo.io")
json_ipinfo = responce_ipinfo.json()
json_ipinfo["ip"] = "hidden"

if __name__ == "__main__":
    for key in json_ipinfo:
        print(key, ":", json_ipinfo[key])
