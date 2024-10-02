import os
import shutil
from utils.speech import speak

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        speak(f"Folder '{folder_name}' created, sir.")
    except FileExistsError:
        speak(f"Folder '{folder_name}' already exists, sir.")

def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        speak(f"Folder '{folder_name}' deleted, sir.")
    except FileNotFoundError:
        speak(f"Folder '{folder_name}' does not exist, sir.")

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("")
        speak(f"File '{file_name}' created, sir.")
    except Exception as e:
        speak(f"Could not create file '{file_name}', sir.")

def delete_file(file_name):
    try:
        os.remove(file_name)
        speak(f"File '{file_name}' deleted, sir.")
    except FileNotFoundError:
        speak(f"File '{file_name}' does not exist, sir.")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        speak(f"Moved file from '{source}' to '{destination}', sir.")
    except FileNotFoundError:
        speak("The source file does not exist, sir.")
    except Exception as e:
        speak("Could not move the file, sir.")
