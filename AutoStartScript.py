import subprocess
from pathlib import Path

print('установка зависимостей...')
subprocess.run(['sudo', 'apt', 'install', 'paplay',])


# получение имени текущенго пользователя и пути к директории
PATH_TO_SRCIPT = Path(__file__)
PATH_TO_FOLDER_WITH_SRCIPT = PATH_TO_SRCIPT.parent
USER = subprocess.run(['whoami'], capture_output=True, text=True).stdout
print(USER[:-1])

# создание AlertLowBattery.service в /etc/systemd/system
subprocess.run(['mkdir', '-p', f'/home/{USER[:-1]}/.config/systemd/user/system',])
with open('AlertLowBattery.service', 'w') as file_service:
    file_service.write(
f"""
[Unit]
Description=AlertLowBattery
After=sound.target pipewire.service pipewire-pulse.service wireplumber.service

[Service]
ExecStart=/usr/bin/python3 {PATH_TO_SRCIPT}
Type=simple
User={USER[:-1]}
WorkingDirectory={PATH_TO_FOLDER_WITH_SRCIPT}

[Install]
WantedBy=multi-user.target
"""
)
subprocess.run(['cp', 'AlertLowBattery.service', '~/.config/systemd/user/AlertLowBattery.service'])
    

# перезагрузка демона и настройка авто запуска скрипта
subprocess.run(['systemctl', '--user', 'daemon-reload',])
subprocess.run(['systemctl', '--user', 'enable', 'AlertLowBattery.service',])
subprocess.run(['systemctl', '--user', 'start', 'AlertLowBattery.service',])
subprocess.run(['systemctl', '--user', 'status', 'AlertLowBattery.service',])
