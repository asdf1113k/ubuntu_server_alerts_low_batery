from colorama import init, Fore
init(autoreset=True)

def filter_color(obj: int | float | str):
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
          
def filter_color2(obj):
     ...
     