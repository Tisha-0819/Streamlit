# Task 3: Create a Streamlit app that uses Hugging Face to generate text from a prompt.

import streamlit as st
from transformers import pipeline

# App title
st.title("🤖 Hugging Face Text Generator")

# Load model (cached automatically)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# User input
prompt = st.text_area("Enter your prompt")

# Button
if st.button("Generate Text"):
    if prompt:
        with st.spinner("Generating text..."):
            result = generator(prompt, max_length=100, num_return_sequences=1)
            st.success("Generated Text:")
            st.write(result[0]["generated_text"])
    else:
        st.warning("Please enter a prompt")
