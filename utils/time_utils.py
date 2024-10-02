from datetime import datetime

def check_time(time_str):
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
        return time_obj
    except ValueError:
        return None
