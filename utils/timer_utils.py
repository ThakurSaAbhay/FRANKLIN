import time
import winsound
from utils.speech import speak

def set_timer(seconds):
    speak(f"Timer set for {seconds} seconds, sir.")
    time.sleep(seconds)
    winsound.Beep(1000, 1000)  # Frequency 1000Hz, Duration 1000ms (1 second)
    speak("Time's up, sir!")

def set_reminder(reminder_message, seconds):
    speak(f"Reminder set: {reminder_message}, in {seconds} seconds.")
    time.sleep(seconds)
    winsound.Beep(1000, 1000)  # Frequency 1000Hz, Duration 1000ms (1 second)
    speak(f"Sir, this is your reminder for {reminder_message}")
