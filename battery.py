import psutil
import time
from com import speak

# reminders for battery
class battery_reminder():

    '''This class is used to check the battery percentage of the device 
    and remind the user to charge or unplug the device based on the battery percentage'''

    def __init__(self):
        pass

    def check_battery(self):
        battery = psutil.sensors_battery()
        percent = battery.percent
        return percent

    def battery(self):
        low_battery_threshold = 20
        high_battery_threshold = 80
        
        while True:
            battery_percent = self.check_battery()
            if battery_percent <= low_battery_threshold:
                speak(f"Sir, the device battery is at {battery_percent}%. Please charge your device.")

            if battery_percent >= high_battery_threshold:
                speak(f"sir, the device battery is at {battery_percent}%. Please unplug your device.")
            
            time.sleep(100)  # Check every minute

