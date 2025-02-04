import time
import plyer
from com import speak
from datetime import datetime

def send_remind(task):
    plyer.notification.notify(
        title = "Reminder",
        message = task,
        timeout = 10
    )

def reminder(task, reminder_time):
    try:

        current_time = datetime.now().strftime("%H:%M")
        while current_time != reminder_time:
            current_time = datetime.now().strftime("%H:%M")
            time.sleep(1)
        send_remind(task)

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't set the reminder")

# reminder()
