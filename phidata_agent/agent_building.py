from phi.agent import Agent
from phi.model.groq import Groq
from tools_tested import send_email, get_current_weather, get_person_info
from dotenv import load_dotenv

load_dotenv()

content_retriever = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[get_person_info, get_current_weather, send_email],
    instructions=[
        "Only use the send_email tool if the user explicitly asks to send an email or mentions sending an email in their request or else just talk normally",
        "if user wants to send mail to all, then get all the information from get_person_info and in that i have email id and call send email functions for each of them and give peronal recommendations and send mails indivudual recommendations body content based on thier specific information. Don't send same content to everyone"
        "First, use get_person_info to get the person's data based on the name.",
        "Then, use get_current_weather to get weather data for their location.",
        "Based on the weather and character, make recommendations (food, habits, health) in your response.",
        "Do not send emails unless the user clearly requests it."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

while True:
    prompt = input("Enter prompt >> ")
    if prompt == 'Q':
        break
    content_retriever.print_response(prompt)

print("Thank for using us!")