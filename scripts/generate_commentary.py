from dotenv import load_dotenv
import os
from groq import Groq
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompts.prompt_generator import generate_prompt


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

prompt: str = generate_prompt(commentator="Ravi Shastri", event="six", start_time=2.3,
                            end_time=16.6, tts_speed=2.5, 
                            player_names = {
                                "batsman" : "Virat",
                                "bowler" : "Dhoni"

                            },
                            context = {
                                "batting_team" : "Royal Challengers Bangalore",
                                "bowling_team" : "Chennai super kings",
                                "over" : 17.2,
                                "req_runrate" : 8.5,
                                "current_score" : "142/4"
                            })

# Collecting response (testing)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)