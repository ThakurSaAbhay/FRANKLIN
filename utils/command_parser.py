import re

def extract_time_from_command(command):
    time_units = {"second": 1, "minute": 60, "hour": 3600}
    match = re.search(r"(\d+)\s*(second|minute|hour)", command)
    
    if match:
        time_value = int(match.group(1))
        unit = match.group(2)
        return time_value * time_units[unit]
    
    return None

def extract_reminder_from_command(command):
    time_units = {"second": 1, "minute": 60, "hour": 3600}
    
    # Extract the task
    task_match = re.search(r"remind me to (.+?) in", command)
    task = task_match.group(1) if task_match else "something"
    
    # Extract the time
    time_match = re.search(r"in (\d+)\s*(second|minute|hour)", command)
    
    if time_match:
        time_value = int(time_match.group(1))
        unit = time_match.group(2)
        return task, time_value * time_units[unit]
    
    return task, None
