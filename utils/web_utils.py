import webbrowser
import pywhatkit as kit
from utils.speech import speak

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching the web for {query}, sir.")

def open_website(website):
    url = f"http://{website}"
    webbrowser.open(url)
    speak(f"Opening {website}, sir.")

def play_youtube_video(video_name):
    kit.playonyt(video_name)
    speak(f"Playing {video_name} on YouTube, sir.")
