import speech_recognition as sr
import winsound
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        winsound.Beep(500,1000)
        recognizer.adjust_for_ambient_noise(source) 
        try:
            audio = recognizer.listen(source) 
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry sir, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results. Check your internet connection.")
            return ""
