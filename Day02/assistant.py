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
messages=[]
while True:
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
