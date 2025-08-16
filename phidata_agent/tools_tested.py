import requests
from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import json


load_dotenv()

# Send mail
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
        return "Email sent successfully!"
    except Exception as e:
        return "Error sending email:", e


# get weather
def get_current_weather(location: str) -> str:
    """
    Tool Name: get_current_weather

    Description:
        This tool retrieves the current weather information for a specified location using the OpenWeatherMap API.
        It takes a location string (such as a city name or "City,CountryCode") as input and returns weather data in JSON format.
        The tool requires an environment variable 'WEATHER_API_KEY' to be set with a valid OpenWeatherMap API key.

    Inputs:
        - location (str): The name of the city or "City,CountryCode" (e.g., "London,UK").

    Outputs:
        - str: A JSON string containing the weather data for the specified location, or an error message if the request fails.

    Usage Example:
        weather = get_current_weather("Thandalam")
        print(weather)
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": os.getenv("WEATHER_API_KEY"),
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return json.dumps(response.json())
    except requests.RequestException as e:
        return json.dumps({"error": str(e)})
    
# In-memory database of persons
PERSON_DATABASE = [
    {
        "name": "Sivabalan T",
        "email": "221501138@rajalakshmi.edu.in",
        "character_info": "Curious, hardworking, and passionate about AI.",
        "location": ",Thandalam, Chennai, India"
    },
    {
        "name": "Yudeeswaran",
        "email": "221501182@rajalakshmi.edu.in",
        "character_info": "Curious, staying in hostel, Focusing on placement, AI enthusiast, always using phone, lean",
        "location": "Thandalam, Chennai, India"
    },
    {
        "name": "Shrinithi",
        "email": "221501135@rajalakshmi.edu.in",
        "character_info": "Staying in home with family, Care taker, commited, hosnest girl, cute face, focusing on career and boyfriend",
        "location": "Poonamalle, Chennai, India"
    },
    {
        "name": "Sriram",
        "email": "221501135@rajalakshmi.edu.in",
        "character_info": "Curious, staying in hostel, always using phone, health worst, in medication, gym boy, GATE preparation, Love failure",
        "location": "Thandalam, Chennai, India"
    },
    {
        "name": "Sharukesh",
        "email": "221501130@rajalakshmi.edu.in",
        "character_info": "Hard worker, non stop talker, studying for placement, not focusing on health, late night sleep",
        "location": "Thandalam, Chennai, India"
    },
    # Add more person records as needed
]

def get_person_info(name: str) -> str:
    """
    Tool Name: get_person_info
    Available names: Sivabalan T, Yudeeswaran, Shrinithi, Sharukesh, Sriram
    Description:
        This tool retrieves information about a person from the in-memory database based on the provided name.
        It returns the person's name, email, character_info, and location if found.

    Inputs:
        - name (str): The name of the person to search for.

    Outputs:
        - str: A JSON string containing the person's data if found, or an error message if not found.

    Usage Example:
        person = get_person_info("Sivabalan T")
        print(person)
    """
    for person in PERSON_DATABASE:
        if person["name"].lower() == name.lower():
            return json.dumps(person)
    return json.dumps({"error": f"No data found for name: {name}"})

