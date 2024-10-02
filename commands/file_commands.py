import os
from utils.speech import speak

def open_file():
    speak("Which file would you like to open, sir?")
    file_path = input("Enter full file path: ")  # Future improvement: browse files via voice
    try:
        os.startfile(file_path)
        speak(f"Opening {file_path}")
    except Exception as e:
        print(e)
        speak("Sorry sir, I couldn't open the file.")
