import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key = "API-KEY-HERE")

# Define function to get advice from the AI model based on user input
def get_energy_advice(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[ 
                {"role": "system", "content": "You are an expert in energy efficiency, renewable energy sources, and cost-saving strategies related to energy consumption. Provide detailed advice, tips, and innovative solutions to reduce energy bills and enhance sustainability."},
                {"role": "user", "content": prompt} 
            ]
        )
        # Extract the AI's response from the received data
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app setup begins here
with st.form("query_form"):
    # A text area in the form for users to type their query
    prompt = st.text_area("Enter a query about energy consumption:", "", 
                          help="Ask about reducing energy costs, improving home insulation, or choosing energy-efficient appliances.")
    submit_button = st.form_submit_button(label="Get Advice")

if submit_button and prompt:
    advice = get_energy_advice(prompt)
    st.write("Energy Saver's advice:", advice)
