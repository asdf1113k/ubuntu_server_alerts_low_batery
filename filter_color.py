from colorama import init, Fore
init(autoreset=True)

def filter_color(obj: str | int | float) -> str:
     match obj:
          case 'ясно':
               return Fore.YELLOW + obj

          case 'переменная облачность' | 'облачно' | 'небольшая облачность' | 'облачно с прояснениями':
               return Fore.WHITE + obj
          
          case obj if obj < 0:
               return Fore.BLUE + str(obj)
          
          case obj if obj <= 10:
               return Fore.CYAN + str(obj)
          
          case obj if obj > 10:
               return Fore.YELLOW + str(obj)

          case _:
               return obj
     

def filter_color_old_version(obj: int | float | str) -> str:
     """это версия функции больше не используеться, остаеться здесь как экспанат в музее
     ну или если у когото в друг будет версия python>3.10"""
     if isinstance(obj, str):
          if obj in ['ясно']:
               return Fore.YELLOW + obj
          elif obj in ['переменная облачность', 'облачно']:
                return Fore.WHITE + obj
          else:
               return obj

     if isinstance(obj, (int, float)):  
          if obj > 10:
               return Fore.YELLOW + str(obj)
          elif obj <= 10:
               return Fore.CYAN + str(obj)
          elif obj <= 0:
               return Fore.BLUE + str(obj)
          else:
               return obj
          
