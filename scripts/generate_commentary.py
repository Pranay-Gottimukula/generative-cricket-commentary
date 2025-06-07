from dotenv import load_dotenv
import os
from groq import Groq
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompts.prompt_generator import generate_user_prompt, generate_system_prompt


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

user_prompt: str = generate_user_prompt(event="six", start_time=2.3,
                            end_time=16.6, tts_speed=2.5, 
                            )

system_prompt: str = generate_system_prompt(commentator="Ravi Shastri",
                            context = {
                                "batsman" : "Virat",
                                "bowler" : "Dhoni",
                                "batting_team" : "Royal Challengers Bangalore",
                                "bowling_team" : "Chennai super kings",
                                "over" : 17.2,
                                "required_run_rate" : 8.5,
                                "current_score" : "142/4"
                            })

# Collecting response (testing)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
)

commentary_text: str = chat_completion.choices[0].message.content
print(chat_completion.choices[0].message.content)