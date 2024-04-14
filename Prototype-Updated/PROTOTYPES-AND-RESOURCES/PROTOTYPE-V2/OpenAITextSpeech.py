from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key="API-KEY-HERE")

# Ask the user to enter a filename for the audio file
filename = input("Please enter a name for the audio file: ")
complete_filename = f"{filename}.mp3"

# Define where the audio file will be saved on the computer
# Users provide the file name each time the code is run
speech_file_path = Path(rf"./PROTOTYPES-&-RESOURCES/PROTOTYPE-V2/audio/{complete_filename}")

# Ensures that the folder we want to save the file in exists
speech_file_path.parent.mkdir(parents=True, exist_ok=True)

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",  # Voice model options: alloy, echo, fable, onyx, nova, shimmer (included tests in 'audio' file)
    input="Hello there! As a sustainability assistant, I can help you reduce your energy bills and live a more eco-friendly lifestyle. Please feel free to ask me any questions you may have."  # Insert text you want to convert to speech
)

# Open a file to save the speech audio
# The format of audio files is 'wb'
with open(speech_file_path, 'wb') as audio_file:
    audio_file.write(response.content)  # Save the generated speech from OpenAI into the file

# Print message to notify the audio file has been saved successfully
print(f"Audio file saved at: {speech_file_path}")
