prossent_batery = upower -i $(upower -e | grep 'BAT') | grep percentage | awk '{print $2}'
echo $prossent_batery