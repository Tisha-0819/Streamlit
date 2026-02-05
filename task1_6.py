# Task 1: Create a "Hello AI" Streamlit app with user input and text output.

import streamlit as st

# App title
st.title("Hello AI")

# User input
name = st.text_input("Enter your name")

# Button action
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}! Welcome to the AI world 🚀")
    else:
        st.warning("Please enter your name")
