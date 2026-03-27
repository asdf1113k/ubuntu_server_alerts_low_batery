import subprocess
from pathlib import Path

print('установка зависимостей...')
subprocess.run(['sudo', 'apt', 'install', 'paplay',])


# получение имени текущенго  пользователя и пути к директории
PATH_TO_SRCIPT = Path(__file__)
PATH_TO_FOLDER_WITH_SRCIPT = PATH_TO_SRCIPT.parent
USER = subprocess.run(['whoami'], capture_output=True, text=True)
print(USER)

# копирование AlertLowBattery.service в /etc/systemd/system
subprocess.run(['mkdir', '-p', '~/.config/systemd/user/',])
with open('~/.config/systemd/user/AlertLowBattery.service', 'w') as file_service:
    file_service.write(
f"""
[Unit]
Description=AlertLowBattery
After=sound.target pipewire.service pipewire-pulse.service wireplumber.service

[Service]
ExecStart=/usr/bin/python3 {PATH_TO_SRCIPT}
Type=simple
User={USER}
WorkingDirectory={PATH_TO_FOLDER_WITH_SRCIPT}

[Install]
WantedBy=multi-user.target
"""
)

    

# перезагрузка демона и настройка авто запуска скрипта
subprocess.run(['sudo', 'systemctl', '--user', 'daemon-reload',])
subprocess.run(['sudo', 'systemctl', '--user', 'enable', 'AlertLowBattery.service',])
subprocess.run(['sudo', 'systemctl', '--user', 'start', 'AlertLowBattery.service',])
subprocess.run(['sudo', 'systemctl', '--user', 'status', 'AlertLowBattery.service',])
