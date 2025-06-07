# Function to generate Prompt

'''
    Inputs given are action happened, timestamps(start, end),
    batsman, bowler, current score, over, required run rate, commentator, player names,
    team names
'''

def generate_user_prompt(event: str, start_time: float, end_time: float,
                   tts_speed: float, context: dict = None):
    time_duration: float = end_time - start_time
    max_words: int = time_duration * tts_speed
    user_prompt =  f"""Generate a exciting and natural-sounding commentary commentary for the following event: "{event}".
    The commentary should be natural, engaging and reflect live match excitment.
    🕒 Duration: {time_duration:.2f} seconds
    📊 Target words: ≤ {max_words} (for {tts_speed:.2f} words/sec TTS speed)
    🎙️ Tone: Lively, expressive, with exclamations, pauses, and vivid cricket-specific language.
    - Ensure it sounds like a real human commentator reacting to the event in real time.
    - Use **exclamation marks**, **commas**, and **periods** everytime there should be a pause to guide the tts for generating good pauses.
    - Use repetition of letters in a word to express emotion and emphasis wherever needed, for example, use "siixxx!" instead of "six!" or use "Wonnnderfullll!" instead of "Wonderfull!.
    - Remember that fullstops, commas and exclaimation marks should not repeate, for example, use "." instead of "..."
    - Don't use numerical symbols. """
    return user_prompt

def generate_system_prompt(commentator: str, context: dict = None):
    system_prompt =  f"""You are a professional cricket commentator, speaking as "{commentator}".
    Take {context} as match context which is in the form of a Python dictionary, where:
    - Keys are match elements (like 'batsman', 'bowler', 'over', 'required_run_rate', etc.).
    - Values describe their current state.
    - Any value set to "None" means no information is available about that attribute.

    Use the context to guide your commentary and stay relevant to what's happening on the field."""
    return system_prompt