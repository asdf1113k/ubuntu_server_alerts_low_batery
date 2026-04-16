"""
скрипт который сам добавит AlertLowBattery.py
в автозапуск systemctl --user
"""

from pathlib import Path
import os
import getpass

class SystemError(Exception):
    pass

if os.name == 'posix':
    pass
elif os.name == "nt":
    raise SystemError('it script not excpected is system')
else:
    raise SystemError('эта система не известна скрипту')

path_to_script = Path(__file__)
path_to_script = path_to_script.parent
PATH_TO_FOLDER_WITH_SRCIPT = path_to_script # получение пути к директории
path_to_script = path_to_script / 'AlertLowBattery.py' # получение пути к файлу AlertLowBattery.py

USERNAME = getpass.getuser() # получение имени пользователя

if __name__ == "__main__":
    print(f'пользователь: {USERNAME}')
    print('установка зависимостей...')
    os.system('sudo apt install pulseaudio-utils')
    os.system('sudo apt install beep')

    os.system(f'mkdir -p /home/{USERNAME}/.config/systemd/user/') # создание папок '~/.config/systemd/user/'
    os.system(f'sudo chown {USERNAME}:{USERNAME} /home/{USERNAME}/.config/systemd/user') # выдача прав доступа к каталогу
    with open('AlertLowBattery.service', 'w') as file_service:
        file_service.write(
    f"""
[Unit]
Description=AlertLowBattery
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {path_to_script}
WorkingDirectory={PATH_TO_FOLDER_WITH_SRCIPT}
Restart=always
RestartSec=5s

[Install]
WantedBy=default.target
"""
)
        file_service.close()
    # копирование AlertLowBattery.service в ~/.config/systemd/user/
    os.system(f'cp -v /{PATH_TO_FOLDER_WITH_SRCIPT / 'AlertLowBattery.service'} /home/{USERNAME}/.config/systemd/user/')
        
    os.system('systemctl --user daemon-reload') # перезагрузка демона
    os.system('systemctl --user enable --now AlertLowBattery.service') # настройка авто запуска скрипта
    os.system('systemctl --user start AlertLowBattery.service') # запуск скрипта в фоновом режиме
    os.system('systemctl --user status AlertLowBattery.service') # проверка статуса скрипта

    print(f"путь до скрипта {path_to_script}")