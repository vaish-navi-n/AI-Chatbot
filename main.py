from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

load_dotenv()

# Initialize Chat gemini-1.5-pro-latest
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-pro-latest') 

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display Form Title
st.title("Chat with Gemini-1.5-pro Model") #Change title to show the correct model.

# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("Ask me something...!"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)

    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt)

    # Display last
    with st.chat_message("assistant"):
        st.markdown(response.text)
