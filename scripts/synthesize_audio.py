import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_audio(text: str = "Let's go and complete this project"):
    tts = TTS(model_name='tts_models/en/ek1/tacotron2').to(device)
    tts.tts_to_file(text=text, file_path="data/output/output.wav")
    return "data/output/output.wav"

audio = generate_audio()
print(audio)