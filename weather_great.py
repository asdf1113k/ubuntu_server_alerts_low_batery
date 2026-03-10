from colorama import init, Fore

init(autoreset=True)

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