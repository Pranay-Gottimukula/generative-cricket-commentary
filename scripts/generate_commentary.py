from dotenv import load_dotenv
import os
from groq import Groq

'''
    This code generates text

    Using Groq API for generating commentary text
'''

# Loads secret key from .env file
load_dotenv()

# Setting up Groq
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

# Collecting response (testing)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)