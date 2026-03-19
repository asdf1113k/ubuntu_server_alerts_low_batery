from colorama import init, Fore
init(autoreset=True)

def filter_color(obj: str | int | float) -> str:
     match obj:
          case 'ясно':
               return Fore.YELLOW + obj

          case 'переменная облачность' | 'облачно' | 'небольшая облачность' | 'облачно с прояснениями' | 'пасмурно':
               return Fore.WHITE + obj
          
          case obj if obj < 0:
               return Fore.BLUE + str(obj)
          
          case obj if obj <= 10:
               return Fore.CYAN + str(obj)
          
          case obj if obj <= 20:
               return Fore.YELLOW + str(obj)
          
          case obj if obj <= 30:
               return Fore.RED
               
          case obj if obj <= 40:
               return Fore.LIGHTRED_EX + str(obj)

          case _:
               return obj
