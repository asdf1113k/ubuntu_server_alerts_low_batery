import asyncio
import os
import requests as rq

try:
    from colorama import init, Fore
    import gpsd
    import winsdk.windows.devices.geolocation as wdg
except ImportError:
    print("установите зависимости командой 'pip install -r requirements.txt' или 'uv sync'")
    print("может быть такое что некоторые импорты не нужны, так что можно не беспокоиться")
init(autoreset=True)
#будет выполняться если не получилось получить доступ к точному местуположению
def get_coordinates_ipinfo():
    responce_ipinfo = rq.get("https://ipinfo.io")
    json_ipinfo = responce_ipinfo.json()
    json_ipinfo['ip'] = 'hidden'
    loc_ipinfo:str   = json_ipinfo["loc"]
    loc_ipinfo:tuple = tuple(loc_ipinfo.split(","))
    return loc_ipinfo


def get_coordinates_linux():
    try:
        gpsd.connect()
        packet = gpsd.get_current()
        if packet.mode >= 2:
            print(f"Широта: {packet.lat}, Долгота: {packet.lon} - gpsd-py3 linux")
            return packet.lat, packet.lon
    except ConnectionRefusedError:
        print(Fore.RED + 'gpsd: Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение')


async def get_coordinates_windows() -> tuple:
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return pos.coordinate.latitude, pos.coordinate.longitude



def get_coordinates():
    """делает запрос на получение координат у устройства"""
    try:
        if os.name == "nt":
            return asyncio.run(get_coordinates_windows())
        elif os.name == "posix":
            return get_coordinates_linux()
        else:
            return get_coordinates_ipinfo
    except ...:
            ...


if __name__ == '__main__':
    print(get_coordinates())
    