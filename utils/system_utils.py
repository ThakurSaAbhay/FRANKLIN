import os
import psutil
import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from utils.speech import speak

def shutdown_system():
    speak("Shutting down the system, sir.")
    os.system("shutdown /s /t 1")

def restart_system():
    speak("Restarting the system, sir.")
    os.system("shutdown /r /t 1")

def lock_system():
    speak("Locking the screen, sir.")
    os.system("rundll32.exe user32.dll, LockWorkStation")

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"Sir, the battery is currently at {percent} percent.")
    else:
        speak("Sorry sir, I could not retrieve the battery status.")

def increase_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current_volume + 0.1, 1.0), None)
    speak("Volume increased, sir.")

def decrease_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current_volume - 0.1, 0.0), None)
    speak("Volume decreased, sir.")
    
def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_mute_status = volume.GetMute()
    
    if current_mute_status == 0:  # If not already muted
        volume.SetMute(1, None)
        speak("Volume muted, sir.")
    else:
        speak("Volume is already muted, sir.")
        


def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_mute_status = volume.GetMute()

    if current_mute_status == 1:  # If currently muted
        volume.SetMute(1,None)
        speak("Volume unmuted, sir.")
    else:
        speak("Volume is already unmuted, sir.")

    
def set_brightness(level):
    try:
        sbc.set_brightness(level)
        speak(f"Brightness set to {level} percent, sir.")
    except Exception as e:
        speak("Sorry sir, I couldn't adjust the brightness.")
