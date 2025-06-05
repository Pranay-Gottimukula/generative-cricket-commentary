# Function to generate Prompt

'''
    Inputs given are action happened, timestamps(start, end),
    batsman, bowler, current score, over, required run rate, commentator, player names,
    team names
'''

def generate_prompt(commentator: str, event: str, start_time: float, end_time: float,
                   tts_speed: float, player_names: dict = None,
                   context: dict = None):
    time_duration: float = end_time - start_time
    max_words: int = time_duration * tts_speed
    prompt =  f'Imagine you are {commentator}. The current match is between {context["batting_team"]} and {context["bowling_team"]}. The batsman is {player_names["batsman"]}, and the bowler is {player_names["bowler"]}. During the {context["over"]} over, an event occurred: {event}.The current score is {context["current_score"]}, and the required run rate is {context["req_runrate"]}.This event lasted for approximately {time_duration} seconds. Please generate an exciting and natural-sounding commentary with about {max_words} words to fit the timing for a text-to-speech voice at {tts_speed} words per second.Make it enthusiastic and match the tone of live sports broadcasting.'
    return prompt
