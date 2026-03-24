#!/usr/bin/env python3
import subprocess

result = subprocess.run(['cat', '/sys/class/power_supply/BAT1/capacity'], capture_output=True, text=True)

battery_charge:int = int(result.stdout)
print(battery_charge)