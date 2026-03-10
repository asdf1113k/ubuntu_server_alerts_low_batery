from weather_great import  weather_great_greet_russia

from weather_api_service import json_openweathermap
from coordinates import json_ipinfo

from colorama import init, Fore

def filter_color(obj: int | float | str):
     if isinstance(obj, str):
          if obj in ['переменная облачность', 'облачно']:
                return Fore.WHITE + obj

     if isinstance(obj, (int, float)):  
          if obj <= 10:
               return Fore.CYAN
          elif obj <= 0:
               return Fore.BLUE + obj
          else:
               return obj
            

class weather:
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
        print(f'температура: {filter_color(self.temp)}°C'.rjust(25), end=' ')
        print(f'чуствуеться как: {filter_color(self.temp_feels_like)}°C', end='\n')
        print(f'скорость ветра: {self.wind_speed} м/с'.rjust(25))


    
init(autoreset=True)
if __name__ == "__main__":
    weather_great_greet_russia()
    # ip скрыт в weather_api_service
    # print(json_ipinfo)
    # print(json_openweathermap)
    wt = weather(json_ipinfo, json_openweathermap)
    wt.print_weather()
