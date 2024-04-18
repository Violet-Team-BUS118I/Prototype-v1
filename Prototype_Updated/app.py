import streamlit as st

# Import your actual module names & functions here
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.OpenAITextToSpeech import main as text_to_speech_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V3.SpeechAndChat import main as speech_and_chat_main

# Set up the page configuration
st.set_page_config(page_title='Sustainability Suite', layout='wide')

# Header setup
pages = {
    "Speech and Chat": speech_and_chat_main
}

# Header Menu
tab = st.tabs(["Speech and Chat"])[0]  # Corrected to index the list of tabs

with tab:
    speech_and_chat_main()  # This function is called when the tab is active

# Footer
st.markdown("---")
st.markdown("© 2024 Violet Team")  # Corrected the footer markdown formatting