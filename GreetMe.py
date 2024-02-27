import pyttsx3
import datetime
import hashlib
import getpass
import platform
from Speak import speak
    # Wait for the speech to finish
def check_system():
    # Add checks for system information if needed
    system_info = platform.system()
    speak(f"Checking system... I am running on {system_info}.")

def greet():
    current_time = datetime.datetime.now().time()

    if datetime.time(5, 0) <= current_time < datetime.time(12, 0):
        speak("Good morning, sir. I hope you had a restful night. "
              "I am checking if the system is in good condition.")
    elif datetime.time(12, 0) <= current_time < datetime.time(17, 0):
        speak("Good afternoon, sir. I trust your day has been productive. "
              "I am checking if the system is in good condition.")
    else:
        speak("Good evening, sir. I hope your day was fulfilling. "
              "I am checking if the system is in good condition.")

    speak("Everything seems to be in order. Jarvis is at your service.")



 