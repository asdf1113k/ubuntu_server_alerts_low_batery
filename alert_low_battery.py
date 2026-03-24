#!/usr/bin/env python3
import subprocess
import time


def sound_low_battery():
    subprocess.run(['say', '"low battery"'])

# get battery charge and connected charging(запрос заряда батареи и подключена ли зарядка)
result_capacity = subprocess.run(['cat', '/sys/class/power_supply/BAT1/capacity'], capture_output=True, text=True)
result_online = subprocess.run(['cat', '/sys/class/power_supply/AC1/online'], capture_output=True, text=True)
battery_charge:     int = int(result_capacity.stdout)
connected_charging: int = int(result_online.stdout)
print(battery_charge)

while 1 == 1:
    if battery_charge <= 20 and 0 == connected_charging:
        sound_low_battery()
        time.sleep(2)
    else:
        time.sleep(10)