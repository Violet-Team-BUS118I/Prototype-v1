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
    st.set_page_config(page_title="Energy Bill Analyzer", layout='centered')
    st.title("Energy Bill Analyzer")

    # Instructions
    st.markdown("""
    **About:**
    This tool analyzes your PG&E bill to provide personalized advice on reducing your energy costs.
    It uses OCR technology to extract text from your uploaded bill and an AI model to analyze the content.
                
    **Instructions:**
    - Upload a PDF version of your PG&E bill
    - Ensure the bill is clear to facilitate accurate text extraction
    """)
    
    # File uploader with collapsed label
    uploaded_file = st.file_uploader("", type=['pdf'], label_visibility="collapsed")
    
    if uploaded_file is not None:
        st.write("Click the button below to begin analysis...")
        extracted_text = process_pdf(uploaded_file)
        display_results(extracted_text)

# Opens the uploaded PDF file and extracts text from each page
def process_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype='pdf')
    if len(doc) == 0:
        st.error("The document is empty or could not be loaded.")
        return ""
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
    prompt = "You are a virtual assistant specialized in energy savings. After analyzing the details of the provided utility bill, summarize the key points and offer specific, actionable advice that could help reduce energy costs. Focus on areas where changes can make the most impact according to the usage patterns and data from the bill."
    with st.form("search_file_query_form"):
        submit_button = st.form_submit_button("Analyze")
        if submit_button:
            advice, error = get_energy_advice(prompt, extracted_text)
            if advice:
                st.success("Analysis completed successfully.")
                st.write("", advice)
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
