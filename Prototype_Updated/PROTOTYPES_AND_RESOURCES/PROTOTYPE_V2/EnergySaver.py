# EnergySaver.py
import streamlit as st
from openai import OpenAI

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

# Main function to run in the app.py
def main():
    # st.header('Energy Saver')
    st.markdown("### Energy Saver")
 
    st.write('Ask me about energy efficiency, renewable energy sources, and cost-saving strategies.')
    with st.form("energy_saver_query_form"):
        prompt = st.text_area("Enter your query:", help="Ask about reducing energy costs, improving home insulation, or choosing energy-efficient appliances.")
        submit_button = st.form_submit_button(label="Get Advice")
        if submit_button and prompt:
            advice = get_energy_advice(prompt)
            st.write("Energy Saver's advice:", advice)