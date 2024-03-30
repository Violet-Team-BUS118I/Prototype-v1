#pip3 install openai==0.28 to install the old version
#pip3 install openai --upgrade to install the latest version
#openai migrate to automatically upgrade codebase to use the 1.0.0 interface
import streamlit as st
import openai
import os

openai.api_key = "YOUR_API_KEY_HERE"

# Define function to get advice from the AI model based on user input
def get_fleet_advice(prompt):
    try:
        # Make a request to the OpenAI API using the ChatCompletion model
        response = openai.Completion.create(
            model="gpt-4",  # Specifies we're using the GPT-4 model
            messages=[  # Messages structure the conversation with the AI
                {"role": "system", "content": "You are a highly knowledgeable assistant trained in urban transportation and fleet management."},
                {"role": "user", "content": prompt}  # User's question is inserted here
            ]
        )
        # Extract the AI's response from the received data
        return response.choices[0].message['content']
    except Exception as e:  # If something goes wrong, catch the error and show it
        return f"An error occurred: {str(e)}"

# Streamlit app setup begins here
# This creates a form in the web app where users can enter their questions
with st.form("query_form"):
    # A text area in the form for users to type their query
    prompt = st.text_area("Enter your query for fleet control advice:", 
                          "",  # Default text is empty, so users see a blank box to type in
                          help="Ask about fleet management principles, vehicle maintenance tips, or strategies for operational efficiency.")
    # A button in the form labeled "Get Advice". Clicking this sends the user's query to the AI
    submit_button = st.form_submit_button(label="Get Advice")

# This part checks if the user has clicked the "Get Advice" button and if there's a question entered
if submit_button and prompt:
    # Calls the function defined above to get advice from the AI based on the user's question
    advice = get_fleet_advice(prompt)
    # Displays the AI's advice on the web page
    st.write("Advisor's advice:", advice)
