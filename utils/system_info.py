import psutil
import platform
import speedtest
from utils.speech import speak

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    total, used, free = psutil.disk_usage('/')

    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    
    info = (
        f"System: {system}, Node: {node}, Release: {release}, Version: {version}, "
        f"CPU Usage: {cpu_usage}%, RAM Usage: {ram_usage}%, "
        f"Disk Usage: {used / (1024**3):.2f} GB used out of {total / (1024**3):.2f} GB."
    )
    
    speak(info)

def check_internet_speed():
    st = speedtest.Speedtest()
    speak("Testing internet speed, sir. Please wait...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping

    speed_info = (
        f"Download speed: {download_speed:.2f} Mbps, "
        f"Upload speed: {upload_speed:.2f} Mbps, "
        f"Ping: {ping} ms."
    )
    print(speed_info)
    
    speak(speed_info)
