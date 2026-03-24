import subprocess

capacity_battery:str = subprocess.run(['cat', '/sys/class/power_supply/BAT1/capacity'], capture_output=True, text=True)
capacity_battery:int = int(capacity_battery)
print(capacity_battery)