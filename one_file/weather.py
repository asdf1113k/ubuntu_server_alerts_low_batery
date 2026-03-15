import requests as rq
from colorama import init, Fore

TOKEN = "7549b3ff11a7b2f3cd25b56d21c83c6a"

init(autoreset=True)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  получение координат по ip  !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
responce_ipinfo     = rq.get("https://ipinfo.io")
json_ipinfo         = responce_ipinfo.json()
json_ipinfo["ip"]   = "hidden"

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  обращение к API openweathermap !!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# https://api.openweathermap.org/data/2.5/weather?lat=55.7&lon=37.5&appid=7549b3ff11a7b2f3cd25b56d21c83c6a&lang=ru&units=metric
loc:str     = json_ipinfo["loc"]
loc:list    = loc.split(",")
responce_api_openweather = rq.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={loc[0]}&lon={loc[1]}&appid={TOKEN}&lang=ru&units=metric"
    )
json_openweathermap = responce_api_openweather.json()

if responce_api_openweather.status_code == 200:
    print(Fore.GREEN + 'api.openweathermap.org подключено')
elif responce_api_openweather.status_code <= 400:
    raise('не удалось подкл к api.openweathermap.org')

#!!!!!!!!!!!!!!!!!!!
# вывод в консоль !!
#!!!!!!!!!!!!!!!!!!!

list_text:list = [
r'                                     /$$     /$$                          ',
r'                                    | $$    | $$                          ',
r' /$$  /$$  /$$  /$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$   /$$$$$$ ',
r'| $$ | $$ | $$ /$$__  $$ |____  $$|_  $$_/  | $$__  $$ /$$__  $$ /$$__  $$',
r'| $$ | $$ | $$| $$$$$$$$  /$$$$$$$  | $$    | $$  \ $$| $$$$$$$$| $$  \__/',
r'| $$ | $$ | $$| $$_____/ /$$__  $$  | $$ /$$| $$  | $$| $$_____/| $$      ',
r'|  $$$$$/$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$  | $$|  $$$$$$$| $$      ',
r' \_____/\___/  \_______/ \_______/   \___/  |__/  |__/ \_______/|__/      ',
]

list_color:list = [
Fore.WHITE,
Fore.WHITE,
Fore.WHITE,
Fore.LIGHTBLUE_EX,
Fore.LIGHTBLUE_EX,
Fore.LIGHTBLUE_EX,
Fore.LIGHTRED_EX,
Fore.LIGHTRED_EX,

]

def weather_great_greet():
    for index in range(len(list_text)):
        print(list_text[index])
    

def weather_great_greet_russia():
    for index in range(len(list_text)):
        print(list_color[index] + list_text[index])

def filter_color(obj: str | int | float) -> str:
     match obj:
          case 'ясно':
               return Fore.YELLOW + obj

          case 'переменная облачность' | 'облачно':
               return Fore.WHITE + obj
          
          case obj if obj < 0:
               return Fore.BLUE + str(obj)
          
          case obj if obj <= 10:
               return Fore.CYAN + str(obj)
          
          case obj if obj > 10:
               return Fore.YELLOW + str(obj)

          case _:
               return obj
          

# класс объединяющий весь json и производящий вывод в терминал
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
    # print(json_ipinfo) # было сделано для просмотра json
    # print(json_openweathermap)
    wt = Weather(json_ipinfo, json_openweathermap)
    wt.print_weather()
