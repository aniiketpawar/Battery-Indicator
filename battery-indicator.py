from plyer import notification
import psutil
from time import sleep

while True:
    battery = psutil.sensors_battery()
    life = battery.percent

    if life < 30:
        notification.notify(
            title="Battery Low",
            message="Please connect to a power source!",
            timeout=10
        )
    else:
        notification.notify(
            title="Battery is there",
            message="Keep hustling!",
            timeout=10
        )
    sleep(50)