# OpenAITextSpeech.py
from openai import OpenAI
import streamlit as st
from io import BytesIO

# Function to convert text to speech and return the audio content
def text_to_speech(text, voice='alloy'):
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,  # Voice model options: alloy, echo, fable, onyx, nova, shimmer
        input=text
    )
    return response.content

# Streamlit UI for inputting text and generating audio
def main():
    # st.header('Text to Speech Converter')
    st.markdown("### Text to Speech")

    # User input for the filename
    filename = st.text_input("Enter a filename for the audio file (without extension):")
    
    # Text area for user to enter text
    text = st.text_area("Enter your text to convert to speech:", "Hello there! As a sustainability assistant, I can help you reduce your energy bills and live a more eco-friendly lifestyle. Please feel free to ask me any questions you may have.")

    # Check if the user provided a filename or chose the "No file" option
    if st.button('Convert Text to Speech'):
        if filename:
            audio_content = text_to_speech(text)
            audio_buffer = BytesIO(audio_content)
            st.audio(audio_buffer, format='audio/mp3')
            st.download_button(
                label="Download Audio",
                data=audio_buffer,
                file_name=f"{filename}.mp3",
                mime="audio/mp3"
            )
        else:
            st.error("Please enter a filename for the audio file.")

    if st.button('No File'):
        st.info("No filename provided. Using default settings.")
        audio_content = text_to_speech(text)
        audio_buffer = BytesIO(audio_content)
        st.audio(audio_buffer, format='audio/mp3')
        st.download_button(
            label="Download Audio",
            data=audio_buffer,
            file_name="default_audio.mp3",
            mime="audio/mp3"
        )