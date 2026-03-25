# как работает скрипт
...

# install
```
cd ~
git clone https://github.com/asdf1113k/ubuntu_server_alerts_low_batery.git
cd ubuntu_server_alerts_low_batery
chmod +x AlertLowBattery.py
```

## added in systemctl:
```
sudo nano /etc/systemd/system/AlertLowBattery.service
```

в открывшемся nano вводим этот текст 
не забываем заменить "ваш_пользователь" на ваш username
```
[Unit]
Description=AlertLowBattery

[Service]
ExecStart=/usr/bin/python3 /home/ваш_пользователь/ubuntu_server_alerts_low_batery/AlertLowBattery.py 
Type=simple
User=ваш_пользователь
WorkingDirectory=/home/ваш_пользователь/ubuntu_server_alerts_low_batery

[Install]
WantedBy=multi-user.target
```

сохраняем и выходим (ctrl+x)


обновляем конфигурацию systemd:
```
sudo systemctl daemon-reload
```
добавляем скрипт в авто загрузку:
```
sudo systemctl enable AlertLowBattery.service

sudo systemctl start AlertLowBattery.service
```