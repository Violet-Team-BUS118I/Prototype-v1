import streamlit as st
from openai import OpenAI
from io import BytesIO

def main(api_key):
    client = OpenAI(api_key=api_key)

    assistant = client.beta.assistants.create(
        name="Energy Saver Bot",
        instructions="You are an expert in energy efficiency, renewable energy sources, and cost-saving strategies related to energy use.",
        model="gpt-4-turbo",
    )

    st.markdown("### File Search")
    st.write("Please upload your PG&E bill for detailed analysis and advice on reducing costs.")

    # File upload section
    uploaded_file = st.file_uploader("Upload your document:", type=['pdf', 'txt'])

    if uploaded_file is not None:
        # Save the uploaded file to the server (if necessary)
        with open(f'/tmp/{uploaded_file.name}', 'wb') as f:
            f.write(uploaded_file.getvalue())

        # Upload the user-provided file to OpenAI
        message_file = client.files.create(
            file=open(f'/tmp/{uploaded_file.name}', 'rb'),
            purpose="assistants"
        )

        # Create a thread (without assistant_id)
        thread = client.beta.threads.create()

        with st.form("search_file_query_form"):
            prompt = st.text_area("Enter your query:")
            submit_button = st.form_submit_button(label="Get Advice")
            if submit_button and prompt:
                # Create a message with the model name (assuming gpt-3-turbo here)
                response = client.messages.create(
                    model="gpt-4-turbo",
                    thread_id=thread.id,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                            "attachments": [
                                {"file_id": message_file.id}
                            ],
                        },
                    ]
                )

                if response:
                    st.write("Energy Saver's advice:", response['choices'][0]['message']['content'])
                    audio_content = text_to_speech(client, response['choices'][0]['message']['content'])
                    if audio_content:
                        audio_buffer = BytesIO(audio_content)
                        st.audio(audio_buffer, format='audio/mp3')
                    else:
                        st.error("Failed to process the document and generate advice.")

def text_to_speech(client, text):
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        return response.content
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    main("YOUR-API-KEY")