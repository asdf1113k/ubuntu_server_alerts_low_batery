#!/usr/bin/env python3.10
from weather_great import  weather_great_greet_russia
from filter_color import filter_color

from weather_api_service import json_openweathermap
from coordinates import json_ipinfo

from colorama import init, Fore
init(autoreset=True)

            

class Weather:
    def __init__(self, json_ipinfo, json_api_weather):
        self.region = json_ipinfo['region']
        self.city = json_api_weather['name']
        self.temp = json_api_weather['main']['temp']
        self.temp_feels_like = json_api_weather['main']['feels_like']
        self.weather_description = json_api_weather['weather'][0]['description']
        self.wind_speed = json_api_weather['wind']['speed']

    def print_weather(self):
        print(Fore.GREEN + f'погода в {self.region}, {self.city}')
        print(f'{filter_color(self.weather_description)}'.rjust(30))
        print(f'температура: {filter_color((self.temp))}°C'.rjust(25), end=' ')
        print(f'чуствуеться как: {filter_color(self.temp_feels_like)}°C', end='\n')
        print(f'скорость ветра: {self.wind_speed} м/с'.rjust(25))


    

if __name__ == "__main__":
    weather_great_greet_russia()
    # ip скрыт в coordinates.py
    # print(json_ipinfo)
    # print(json_openweathermap)
    wt = Weather(json_ipinfo, json_openweathermap)
    wt.print_weather()
