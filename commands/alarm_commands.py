import time
import threading
from utils.speech import speak, listen

def set_alarm():
    try:
        speak("Please tell me the time to set the alarm, sir. Say something like '5:30 a.m.'")
        alarm_time = listen()  
        
        time_parts = alarm_time.lower().replace("a.m.", "").replace("p.m.", "").strip().split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        
        if "p.m." in alarm_time.lower() and hour != 12:
            hour += 12
        elif "a.m." in alarm_time.lower() and hour == 12:
            hour = 0

        speak(f"Alarm set for {alarm_time}, sir.")

        def alarm_ringer():
            while True:
                current_time = time.localtime()
                if current_time.tm_hour == hour and current_time.tm_min == minute:
                    speak("Sir, it's time!")
                    break
                time.sleep(60)  
                
        threading.Thread(target=alarm_ringer).start()

    except Exception as e:
        speak("Sorry sir, I couldn't set the alarm.")
        print(e)

