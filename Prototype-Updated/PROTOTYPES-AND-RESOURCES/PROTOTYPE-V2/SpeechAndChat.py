import streamlit as st
from openai import OpenAI
from io import BytesIO
import os

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="API-KEY-HERE")

# Define function to get advice from the AI model based on user input
def get_energy_advice(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in energy efficiency, renewable energy sources, and cost-saving strategies related to energy use."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define function to convert text to speech
def text_to_speech(text):
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        return response.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app setup begins here
with st.form("query_form"):
    prompt = st.text_area("Enter a query about energy consumption:", "", help="Ask about reducing energy costs, improving home insulation, or choosing energy-efficient appliances.")
    submit_button = st.form_submit_button(label="Get Advice")

if submit_button and prompt:
    advice = get_energy_advice(prompt)
    st.write("Energy Saver's advice:")
    st.write(advice)

    if not advice.startswith("An error occurred"):
        audio_content = text_to_speech(advice)
        if not isinstance(audio_content, str):  # Check if audio content is not an error message
            # Create a BytesIO object to write the audio content in memory
            audio_buffer = BytesIO(audio_content)
            
            # Display an audio player and a download button in the Streamlit app
            st.audio(audio_buffer, format="audio/mp3")
            st.download_button(
                label="Download Energy Advice as MP3",
                data=audio_buffer,
                file_name="energy_advice.mp3",
                mime="audio/mp3"
            )
        else:
            st.write(audio_content)
    else:
        st.write(advice)