# Main App
import streamlit as st
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V2.SpeechAndChat import main as speech_and_chat_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V2.EnergySaver import main as energy_saver_main
from PROTOTYPES_AND_RESOURCES.PROTOTYPE_V2.OpenAITextToSpeech import main as ts

st.sidebar.title('Navigation')

if st.sidebar.button('Speech & Chat'):
    speech_and_chat_main()

if st.sidebar.button('Energy Saver'):
    energy_saver_main()

if st.sidebar.button('Text-to-Speech File'):
    ts()