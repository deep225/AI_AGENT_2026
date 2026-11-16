from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
print("*"*40)
print("Chat initialized. Type 'exit' or 'quit' to end the conversation.")
print("*"*40)
roles={
    1:"You are a helpful teacher, teach each concept in a easy to understand way. Keep the response under 250 words and be polite to the students. You teach class 5 to 8.",
    2:"You are an experienced Python developer and a helpful assistant. You will answer questions about Python programming. Explain the concepts to a student doing his masters. He is already good in Python.",
    3:"You are a knowledgeable tour guide, providing interesting information about various places and attractions. Be engaging and informative.Help to plan the tour",
    4:"You are a motivational speaker, inspiring and encouraging others to achieve their goals. Be positive and uplifting."
}
print("Please Enter your choice, Select the number of the role you want to chat with:")
print("1.Teacher")
print("2. Python Developer")
print("3.Tour Guide")
print("4. Motivational Speaker")
choice = int(input("\nYou: "))
messages=[{"role": "system", "content":roles.get(choice,"You are a helpful Aissitent.") }]

while True:
    print("Now, Please Enter your question")
    user_input = input("\nYou: ")
    messages.append({"role": "user", "content": user_input})
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")        
        break

    # Send a question to the AI model and get a response
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    ai_response=response.choices[0].message.content  
    # Display the AI's response
    print("AI:", ai_response)
    messages.append({"role": "assistant", "content": ai_response})
