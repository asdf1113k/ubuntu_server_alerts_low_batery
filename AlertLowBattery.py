#!/usr/bin/env python3
import subprocess
import time


name_dir_info_battery = subprocess.run(['ls', '/sys/class/power_supply/'], capture_output=True, text=True)
name_dir_info_battery = name_dir_info_battery.stdout.split()



def sound_low_battery():
    subprocess.run(['say', '"low battery"'])


while 1 == 1:
    # get battery charge and connected charging(запрос заряда батареи и подключена ли зарядка)
    result_capacity = subprocess.run(['cat', f'/sys/class/power_supply/{name_dir_info_battery[1]}/capacity'], capture_output=True, text=True)
    result_online = subprocess.run(['cat', f'/sys/class/power_supply/{name_dir_info_battery[0]}/online'], capture_output=True, text=True)
    battery_charge:     int = int(result_capacity.stdout)
    connected_charging: int = int(result_online.stdout)

    if battery_charge <= 20 and 0 == connected_charging:
        sound_low_battery()
        time.sleep(2)
    else:
        print(f'{battery_charge}% статус зарядного устройства: {connected_charging}')
        time.sleep(4)