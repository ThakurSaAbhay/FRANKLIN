from utils.speech import speak

def handle_frequent_commands(command):
    commands = {
        "what is your name": "I am Franklin, your voice assistant, sir.",
        "how are you": "I'm just a program, but thanks for asking, sir!",
        "what can you do": "I can help you with setting timers, reminders, opening applications, and much more, sir!"
    }
    
    response = commands.get(command.lower())
    if response:
        speak(response)
