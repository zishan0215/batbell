import os
from time import sleep

def alarm():
    with open('/sys/class/power_supply/BAT0/present') as f:
        present = int(f.read())
    f.close()

    if present == 1:
        with open('/sys/class/power_supply/BAT0/status') as f1:
            status = f1.read()[:-1]

            if status == 'Discharging':
                with open('/sys/class/power_supply/BAT0/capacity') as f2:
                    capacity = int(f2.read())
                    if capacity < 25:
                        print("Battery Low! You should plug in the charger.")
                        os.system('spd-say batterylow')
                        sleep(1)
                        os.system('spd-say ' + str(capacity) + 'percentremaining')
                    else:
                        print("You should be fine for now.")
                f2.close()
        f1.close()

if __name__ == '__main__':
    while True:
        alarm()
        sleep(120)
