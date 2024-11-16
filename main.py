import openai
import pyttsx3
import whisper
import speech_recognition as sr
import torch
import numpy as np
import re
from database import init_db, add_request

# Load Whisper model
audio_model = whisper.load_model("small")

# Initialize OpenAI API key (replace with your key)
openai.api_key = "API key"

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice
engine.setProperty('rate', 150)

# Initialize database
init_db()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to record audio
def record_audio():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        audio = r.listen(source)
        print("Audio captured")
        
        # Convert the audio to numpy array for Whisper
        raw_data = audio.get_raw_data()
        audio_array = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32) / 32768.0
        return audio_array

# Function to transcribe audio using Whisper
def transcribe_audio(audio_array):
    try:
        print("Transcribing...")
        audio_tensor = torch.from_numpy(audio_array)
        result = audio_model.transcribe(audio=audio_tensor, language='english')
        return result.get("text", "").strip()
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""

# Function to process the voice command
def process_command(command):
    print(f"You said: {command}")
    
    # Extract fields using regex
    project_number = re.search(r'project (\d+)', command)
    amount = re.search(r'(\d+)\s*riyals', command)
    reason = "buy tools" if "buy tools" in command or "to buy" in command else None

    # Extracted values
    project_number = project_number.group(1) if project_number else None
    amount = amount.group(1) if amount else None

    # Prompt for missing fields
    if not project_number:
        speak("Can you provide the project number?")
        project_number = transcribe_audio(record_audio())
    if not amount:
        speak("What is the amount you want to request?")
        amount = transcribe_audio(record_audio())
    if not reason:
        speak("What is the reason for the request?")
        reason = transcribe_audio(record_audio())

    # Confirm details
    confirmation_message = (
        f"You are requesting money for project {project_number}, "
        f"amount: {amount} riyals, for {reason}. Do you want to proceed?"
    )
    print(confirmation_message)
    speak(confirmation_message)

    # Listen for confirmation
    confirmation = transcribe_audio(record_audio()).lower()
    print(f"Confirmation received: {confirmation}")

    # Check confirmation response
    if "yes" in confirmation or "confirm" in confirmation or "proceed" in confirmation:
        # Add to database
        if add_request(project_number, amount, reason):
            speak("Request submitted successfully.")
        else:
            speak("Failed to submit the request.")
    else:
        speak("Request canceled.")
        print("Request canceled.")

# Main loop
def main():
    print("Starting your AI voice assistant...")
    while True:
        try:
            # Step 1: Record audio
            audio_array = record_audio()
            
            # Step 2: Transcribe audio
            user_input = transcribe_audio(audio_array)
            if not user_input:
                print("Couldn't understand the input. Please try again.")
                continue

            # Step 3: Process the voice command
            process_command(user_input)

        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
