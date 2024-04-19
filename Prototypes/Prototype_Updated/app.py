import streamlit as st

from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.OpenAITextToSpeech import main as text_to_speech_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.SpeechAndChat import main as speech_and_chat_main
# from Prototypes.Prototype_Updated.FileSearch import main as file_and_search_main
# from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.SearchFile import main as search_file_main

API_KEY = "API-KEY-HERE"

# Set up the page configuration
st.set_page_config(page_title='Sustainability Suite', layout='wide')

# Header Menu
tabs = st.tabs(["Speech and Chat", "File Search", "Search File"])

with tabs[0]:
    speech_and_chat_main(API_KEY)

with tabs[1]:
   file_and_search_main(API_KEY)

# with tabs[2]:
  # search_file_main(API_KEY)

# Footer
st.markdown("---")
st.markdown("© 2024 Violet Team")