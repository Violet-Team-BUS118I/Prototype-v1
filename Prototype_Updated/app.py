import streamlit as st

from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.OpenAITextToSpeech import main as text_to_speech_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.SpeechAndChat import main as speech_and_chat_main

# Define your API key here
API_KEY = "YOUR-API-KEY-HERE"

# Set up the page configuration
st.set_page_config(page_title='Sustainability Suite', layout='wide')

# Header Menu
tab = st.tabs(["Speech and Chat"])[0]

with tab:
    # Pass the API key to the function
    speech_and_chat_main(API_KEY)

# Footer
st.markdown("---")
st.markdown("© 2024 Violet Team")
