#!/home/julio/py3env/bin/python
import psutil
import os
import subprocess


def check():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    if plugged and battery.percent > 80:
        notify('Hey, battery level is {0:.2f}'.format(battery.percent))


def notify(message):
    my_env = os.environ.copy()
    my_env['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'
    subprocess.Popen(
        ['/usr/bin/notify-send', 'BatteryTracker', message], env=my_env)


if __name__ == '__main__':
    check()
