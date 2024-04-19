# Be sure to install 'Tesseract-OCR'
# Run 'pip install PyMuPDF'
import streamlit as st
from openai import OpenAI
import fitz
import pytesseract
from PIL import Image

API_KEY = 'YOUR-API-KEY-HERE'

# Sets up the page configuration and title
def main():
    st.set_page_config(page_title="Energy Bill Analyzer", layout='wide')
    st.markdown("### File Search")
    st.write("Please upload your PG&E bill for detailed analysis and advice on reducing costs.")

    # Creates a file uploader to allow users to upload their energy bill
    uploaded_file = st.file_uploader("Upload your document:", type=['pdf'])
    if uploaded_file is not None:
        # Processes the uploaded PDF and displays the results
        extracted_text = process_pdf(uploaded_file)
        display_results(extracted_text)

 # Opens the uploaded PDF file and extracts text from each page
def process_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype='pdf')
    text = ""
    for page in doc:
        text += extract_text_from_page(page)
    return text

 # Converts a PDF page to an image and uses OCR to extract text from the image
def extract_text_from_page(page):
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return pytesseract.image_to_string(img)

 # Sets up a form for users to submit document for analysis and displays the results
def display_results(extracted_text):
    prompt = "You are a virtual assistant specialized in energy savings. Analyze this utility bill and provide specific, actionable advice on how to reduce energy costs."
    with st.form("search_file_query_form"):
        submit_button = st.form_submit_button("Analyze my bill!")
        if submit_button:
            advice, error = get_energy_advice(prompt, extracted_text)
            if advice:
                st.write("Energy Saver's advice:", advice)
                play_audio(advice)
            else:
                st.error(f"Failed to get advice: {error}")

# Analyzes the extracted text and provides advice
def get_energy_advice(prompt, text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}]
        )
        return response.choices[0].message.content, None
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

 # Converts the text into speech and plays it back to the user
def play_audio(text):
    audio_content = text_to_speech(text)
    if audio_content:
        st.audio(audio_content, format='audio/mp3')
    else:
        st.error("Failed to generate audio.")

# Converts the text to audio
def text_to_speech(text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.audio.speech.create(model="tts-1", voice="nova", input=text)
        return response.content
    except Exception as e:
        return None

if __name__ == "__main__":
    main()
