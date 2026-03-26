import subprocess 
# получение имени текущенго  пользователя и пути к директории
pwd = subprocess.run(['pwd'], capture_output=True, text=True).stdout
user = pwd.split('/')[2]
print(user)

print('установка зависимостей...')
subprocess.run(['sudo', 'apt', 'install', 'paplay',])

with open('AlertLowBattery.service', 'w') as file_service:
    file_service.write(
f"""
[Unit]
Description=AlertLowBattery

[Service]
ExecStart=/usr/bin/python3 {pwd[:-1]}/AlertLowBattery.py
Type=simple
User={user}
WorkingDirectory={pwd}

[Install]
WantedBy=multi-user.target
"""
)
# копирование AlertLowBattery.service в /etc/systemd/system
subprocess.run(['sudo', 'cp', 'AlertLowBattery.service', '/etc/systemd/system/AlertLowBattery.service',])
# перезагрузка демона и настройка авто запуска скрипта
subprocess.run(['sudo', 'systemctl', 'daemon-reload',])
subprocess.run(['sudo', 'systemctl', 'enable', 'AlertLowBattery.service',])
subprocess.run(['sudo', 'systemctl', 'start', 'AlertLowBattery.service',])
subprocess.run(['sudo', 'systemctl', 'status', 'AlertLowBattery.service',])


