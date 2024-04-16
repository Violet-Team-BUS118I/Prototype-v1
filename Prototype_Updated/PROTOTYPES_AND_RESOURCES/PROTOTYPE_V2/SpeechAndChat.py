# SpeechAndChat.py
import streamlit as st
from openai import OpenAI
from io import BytesIO

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="YOUR-API-KEY")

# Function to get advice from the AI model based on user input
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

# Function to convert text to speech
def text_to_speech(text):
    try:
        response = client.audio.speech.create(
            model="text-to-speech",
            voice="nova",
            input=text
        )
        return response.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main function to run in the app.py
def main():
    ##st.header('Speech and Chat')
    st.markdown("### Speech and Chat")
    st.write("Ask me about reducing energy costs, improving home insulation, or energy-efficient appliances.")
    st.write("I will output text and audio.")

    with st.form("speech_chat_query_form"):
        prompt = st.text_area("Enter your query:", "", help="Ask about reducing energy costs, improving home insulation, or choosing energy-efficient appliances.")
        submit_button = st.form_submit_button(label="Get Advice")

        if submit_button and prompt:
            advice = get_energy_advice(prompt)
            st.write("Energy Saver's advice:", advice)

            if not advice.startswith("An error occurred:"):
                audio_content = text_to_speech(advice)
                # Check if audio content is not an error message
                if not isinstance(audio_content, str):
                    audio_buffer = BytesIO(audio_content)
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