import smtplib
from utils.speech import speak

def send_email():
    speak("To whom do you want to send the email?")
    recipient = input("Enter recipient email: ")  # This can be improved with voice recognition later
    speak("What is the subject?")
    subject = input("Enter the subject: ")
    speak("What is the message?")
    message = input("Enter the message: ")

    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, f"Subject: {subject}\n\n{message}")
        server.close()
        speak("Email sent successfully.")
    except Exception as e:
        print(e)
        speak("Sorry sir, I couldn't send the email.")
