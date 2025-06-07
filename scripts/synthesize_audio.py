import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_audio(text: str = "Siixxx. What a shot by Virat. Wonnnderfullll, he's taking the game away from Chennai Super Kings."):

    speaker = "male-en-2"

    tts = TTS(model_name='tts_models/multilingual/multi-dataset/your_tts').to(device)
    tts.tts_to_file(text=text, file_path="data/output/output.wav", speaker=speaker, language="en", speed=0.7)
    return "data/output/output.wav"

audio = generate_audio()
print(audio)