from pathlib import Path
import os
import getpass
print('установка зависимостей...')
os.system('sudo apt install paplay')


# получение имени текущенго пользователя и пути к директории
path_to_script = Path(__file__)
path_to_script = path_to_script.parent
PATH_TO_FOLDER_WITH_SRCIPT = path_to_script
path_to_script = path_to_script / 'AlertLowBattery.py'

USERNAME = getpass.getuser()
print(USERNAME)

# создание AlertLowBattery.service в ~/.config/systemd/user
os.system(f'cd {PATH_TO_FOLDER_WITH_SRCIPT}')
os.system(f'mkdir -p /home/{USERNAME}/.config/systemd/user/')
os.system('sudo chown {USERNAME}:{USERNAME} /home/{USERNAME}/.config/systemd/user') # ДАЮ ПРАВА ПОЛЬЗОВАТЕЛЮ
with open('AlertLowBattery.service', 'w') as file_service:
    file_service.write(
f"""
[Unit]
Description=AlertLowBattery
After=sound.target pipewire.service pipewire-pulse.service wireplumber.service

[Service]
ExecStart=/usr/bin/python3 {path_to_script}
Type=simple
user={USERNAME}
WorkingDirectory={PATH_TO_FOLDER_WITH_SRCIPT}
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
"""
)
    file_service.close()
# копирование AlertLowBattery.service в ~/.config/systemd/USERNAME/
os.system(f'cp -v /{PATH_TO_FOLDER_WITH_SRCIPT / 'AlertLowBattery.service'} /home/{USERNAME}/.config/systemd/user/'   )
    

# перезагрузка демона и настройка авто запуска скрипта
os.system('systemctl --user daemon-reload')
os.system('systemctl --user enable AlertLowBattery.service')
os.system('systemctl --user start AlertLowBattery.service')
os.system('systemctl --user status AlertLowBattery.service')

print(f"путь до скрипта {path_to_script}")