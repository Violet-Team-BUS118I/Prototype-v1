import streamlit as st

from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.OpenAITextToSpeech import main as text_to_speech_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.SpeechAndChat import main as speech_and_chat_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.FileSearch import main as file_and_search_main


# Define your API key here
API_KEY = "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"

# Set up the page configuration
st.set_page_config(page_title='Sustainability Suite', layout='wide')

# Header Menu
tabs = st.tabs(["Speech and Chat", "File Search"])

with tabs[0]:
    speech_and_chat_main(API_KEY)

with tabs[1]:
    file_and_search_main(API_KEY)

# Footer
st.markdown("---")
st.markdown("© 2024 Violet Team")