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
#Send a question to the AI model and get a response
response=client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {"role": "user", "content": "Hello, AI! How are you today?"}
    ]
)   

#Display the AI's response
print(response.choices[0].message.content)