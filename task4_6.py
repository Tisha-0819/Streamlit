# Task 4: Add session state to your app to maintain chat history.

import streamlit as st
from transformers import pipeline

st.title("💬 AI Chat App")

# load model once
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

model = load_model()

# session state for chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

prompt = st.text_input("You")

if st.button("Send") and prompt:
    reply = model(prompt, max_length=60)[0]["generated_text"]
    st.session_state.chat.append(("You", prompt))
    st.session_state.chat.append(("AI", reply))

# display chat history
for user, text in st.session_state.chat:
    st.write(f"**{user}:** {text}")
