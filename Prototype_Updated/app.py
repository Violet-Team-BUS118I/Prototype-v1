import streamlit as st

# Import your actual module names & functions here
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V2.EnergySaver import main as energy_saver_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V2.OpenAITextToSpeech import main as text_to_speech_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V2.SpeechAndChat import main as speech_and_chat_main


# Set up the page configuration
st.set_page_config(page_title='Sustainability Suite', layout='wide')

# Header setup
pages = {
    "Energy Saver": energy_saver_main,
    "Text to Speech": text_to_speech_main,
    "Speech and Chat": speech_and_chat_main
}

# Header Menu
col1, col2, col3 = st.tabs(["Energy Saver", "Text to Speech", "Speech and Chat"])

with col1:
    energy_saver_main()

with col2:
    text_to_speech_main()

with col3:
    speech_and_chat_main()


#  footer
st.markdown("---")
st.markdown("© 2024 Violet Team")