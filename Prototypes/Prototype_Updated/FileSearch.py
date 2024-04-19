# Run 'pip install pdfplumber'
import streamlit as st
from openai import OpenAI
import pdfplumber
from io import BytesIO

API_KEY = 'YOUR-API-KEY-HERE'

def main():
    st.markdown("### File Search")
    st.write("Please upload your PG&E bill for detailed analysis and advice on reducing costs.")

    uploaded_file = st.file_uploader("Upload your document:", type=['pdf'])
    if uploaded_file is not None:
        extracted_text = extract_text_from_pdf(uploaded_file)
        
        prompt = "You are a virtual assistant specialized in energy savings. Analyze this utility bill and provide specific, actionable advice on how to reduce energy costs."

        with st.form("search_file_query_form"):
            submit_button = st.form_submit_button("Analyze my bill!")
            if submit_button:
                advice, error = get_energy_advice(prompt, extracted_text)
                if advice:
                    st.write("Energy Saver's advice:", advice)
                    audio_content = text_to_speech(advice)
                    if audio_content:
                        audio_buffer = BytesIO(audio_content)
                        st.audio(audio_buffer, format='audio/mp3')
                    else:
                        st.error("Failed to generate audio.")
                else:
                    st.error("Failed to get advice: " + error)

def get_energy_advice(prompt, extracted_text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": extracted_text}
            ]
        )
        return response.choices[0].message.content, None
    except Exception as e:
        return None, str(e)

def text_to_speech(text):
    try:
        client = OpenAI(api_key=API_KEY)
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        return response.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

if __name__ == "__main__":
    main()
