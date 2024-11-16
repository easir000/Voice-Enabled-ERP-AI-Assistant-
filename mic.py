import whisper
import torch
import speech_recognition as sr
import numpy as np

# Load Whisper model for multilingual support
audio_model = whisper.load_model("small", device="cpu")

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        audio = recognizer.listen(source)
        raw_data = audio.get_raw_data()
        audio_array = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32) / 32768.0
        return audio_array

def transcribe_audio(audio_array, language="en"):
    audio_tensor = torch.from_numpy(audio_array)
    result = audio_model.transcribe(audio=audio_tensor, language=language)
    return result.get("text", "")
