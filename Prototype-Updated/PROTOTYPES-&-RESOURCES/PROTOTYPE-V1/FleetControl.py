#pip3 install openai --upgrade to install the latest version
#openai migrate to automatically upgrade codebase to use the 1.0.0 interface
import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key = "YOUR-API-KEY")

# Define function to get advice from the AI model based on user input
def get_fleet_advice(prompt):
    try:
        # Make a request to the OpenAI API using the ChatCompletion model
        completion = client.chat.completions.create(
            model="gpt-4",  # Specifies we're using the GPT-4 model
            messages=[  # Messages structure the conversation with the AI
                {"role": "system", "content": "You are a highly knowledgeable assistant trained in urban transportation and fleet management."},
                {"role": "user", "content": prompt}  # User's question is inserted here
            ]
        )
        # Extract the AI's response from the received data
        return completion.choices[0].message.content
    except Exception as e:  # If something goes wrong, catch the error and show it
        return f"An error occurred: {str(e)}"