import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(subject, body, receiver_email):
    """
    Tool Name: send_email

    Description:
        This tool sends an email using the specified SMTP server and credentials.

    Inputs:
        - subject (str): The subject of the email.
        - body (str): The body content of the email. (In end i need signature with regards, Sivabalan T (B-TECH AIML))
        - receiver_email (str): The recipient's email address.

    Outputs:
        - None. Prints success or error message.

    Usage Example:
        send_email(
            subject="Project Update",
            body="The project is on track.",
            receiver_email="manager@example.com",
        )
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "sparkysiva10@gmail.com"         # Replace with your email address
    password = os.getenv('GMAIL_APP_PASSWORD') 
    receiver_email = receiver_email     # Replace with the recipient's email address

    # Email content
    subject = subject
    body = body
    # Create message container
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body to the message
    message.attach(MIMEText(body, "plain"))

    try:
        # Set up the SMTP server and start TLS for security
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

if __name__ == "__main__":
    send_email("He is really great","You are cool","221501138@rajalakshmi.edu.in")