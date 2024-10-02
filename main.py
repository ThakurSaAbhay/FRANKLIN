from utils.speech import speak, listen
from utils.apps_utils import open_application
from utils.web_utils import search_web, open_website, play_youtube_video
from utils.file_utils import create_folder, delete_folder, create_file, delete_file, move_file
from utils.system_utils import shutdown_system, restart_system, lock_system, get_battery_status, increase_volume, decrease_volume, mute_volume,unmute_volume, set_brightness
from utils.timer_utils import set_timer, set_reminder
from utils.command_parser import extract_time_from_command, extract_reminder_from_command
from utils.system_info import get_system_info, check_internet_speed
from commands.frequently_used_commands import handle_frequent_commands
from commands.email_commands import send_email
from commands.alarm_commands import set_alarm
from commands.file_commands import open_file
from commands.web_commands import open_browser
def main():
    speak("Hello sir, how can I assist you today?")
    
    while True:
        command = listen()
        
        if "email" in command:
            send_email()
        elif "set an alarm" in command:
            set_alarm()
        elif "find a file" in command:
            open_file()
        elif "open browser" in command:
            open_browser()
        elif "shutdown" in command:
            shutdown_system()
        elif "restart" in command:
            restart_system()
        elif "lock" in command:
            lock_system()
        elif "battery" in command:
            get_battery_status()
        elif "increase volume" in command:
            increase_volume()
        elif "decrease volume" in command:
            decrease_volume()
        elif "mute volume" in command:
            mute_volume()
        elif "Unmute please" in command:
            unmute_volume()
        elif "brightness" in command:
            # Example: "Set brightness to 50 percent"
            try:
                brightness_level = int(command.split()[-1])  # Get the number from command
                set_brightness(brightness_level)
            except ValueError:
                speak("Sorry sir, I didn't catch the brightness level.")
        
        elif "create folder" in command:
            folder_name = command.split("create folder")[-1].strip()
            create_folder(folder_name)

        elif "delete folder" in command:
            folder_name = command.split("delete folder")[-1].strip()
            delete_folder(folder_name)

        elif "create file" in command:
            file_name = command.split("create file")[-1].strip()
            create_file(file_name)

        elif "delete file" in command:
            file_name = command.split("delete file")[-1].strip()
            delete_file(file_name)

        elif "move file" in command:
            try:
                source, destination = command.split("move file")[-1].strip().split("to")
                move_file(source.strip(), destination.strip())
            except ValueError:
                speak("Sorry sir, I didn't understand the file paths.")
        
        elif "search the web for" in command:
            query = command.split("search the web for")[-1].strip()
            search_web(query)

        elif "open website" in command:
            website = command.split("open website")[-1].strip()
            open_website(website)

        elif "play" in command and "on youtube" in command:
            video_name = command.split("play")[-1].strip().replace("on youtube", "").strip()
            play_youtube_video(video_name)
            
        elif "open" in command:
            app_name = command.split("open")[-1].strip()
            open_application(app_name)

        elif "timer" in command:
            seconds = extract_time_from_command(command)  # Implement this to extract time
            set_timer(seconds)
        elif "remind me" in command:
            reminder_message, seconds = extract_reminder_from_command(command)  # Implement this to extract
            set_reminder(reminder_message, seconds)
            
        elif command.lower() in ["what is your name", "how are you", "what can you do"]:
            handle_frequent_commands(command)
        
        elif "system info" in command:
            get_system_info()
        elif "internet speed" in command:
            check_internet_speed()

        elif "exit" in command or "stop" in command or "rest" in command:
            speak("Goodbye sir.")
            break
    
    speak("Would you like to restart conversation, sir?")
    restart_command = listen()
    
    if "yes" in restart_command or "restart" in restart_command or "wake up daddy's home" in restart_command:
        restart_franklin()

def restart_franklin():
    speak("Welcome back, sir.")
    main()

if __name__ == "__main__":
    main()
