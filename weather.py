from weather_great import weather_great

from weather_api_service import json_openweather
from coordinates import json_ipinfo

from colorama import init

init(autoreset=True)
if __name__ == "__main__":
    weather_great()
    print(json_ipinfo)
    print(json_openweather)
