import streamlit as st
from openai import OpenAI
from io import BytesIO

# Initialize main interface of application and take an API key to interact with OpenAI API
def main(api_key):
    client = OpenAI(api_key=api_key)

    # Setup the main page with a title and introductory text
    st.markdown("### Speech and Chat")
    st.write("Ask me about reducing energy costs, improving home insulation, or energy-efficient appliances.")
    st.write("I will output text and audio.")

    # Create a form for users to input their queries
    with st.form("speech_chat_query_form"):
        prompt = st.text_area("Enter your query:", "", help="Ask about reducing energy costs, improving home insulation, or choosing energy-efficient appliances.")
        submit_button = st.form_submit_button(label="Get Advice")

        # Process the user's query upon form submission
        if submit_button and prompt:
            advice = get_energy_advice(client, prompt)
            st.write("Energy Saver's advice:", advice)

            # If no errors occurred, convert the advice to audio
            if not advice.startswith("An error occurred:"):
                audio_content = text_to_speech(client, advice)
                if not isinstance(audio_content, str):
                    audio_buffer = BytesIO(audio_content)
                    st.audio(audio_buffer, format="audio/mp3")
                else:
                    st.write(audio_content) # If an error occurred during audio generation, display the error
            else:
                st.write(advice)  # If an error occurred during advice generation, display the error

# Get advice from OpenAI based on the user's input
def get_energy_advice(client, prompt):
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

# Convert text into speech
def text_to_speech(client, text):
    try:
        response = client.audio.speech.create(
            model="tts-1", 
            voice="nova",   
            input=text     
        )
        return response.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
