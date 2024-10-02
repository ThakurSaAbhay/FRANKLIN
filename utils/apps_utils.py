import ctypes
import os
from utils.speech import speak

def open_application(app_name):
    try:
        app_name = app_name.lower()
        ctypes.windll.shell32.ShellExecuteW(None, "open", app_name, None, None, 1)
        speak(f"Opening {app_name}, sir.")
    except Exception as e:
        speak(f"Sorry sir, I couldn't open {app_name}. Please make sure it is installed.")
