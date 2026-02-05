# Task 5: Create a chat app from a PDF and other file formats and respond for doc.

import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

st.title("📄 Document Chat App")

# load model once
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

model = load_model()

# session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# upload file
file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

doc_text = ""
if file:
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        for page in pdf.pages:
            doc_text += page.extract_text()
    else:
        doc_text = file.read().decode("utf-8")

question = st.text_input("Ask from document")

if st.button("Ask") and question:
    prompt = doc_text[:1000] + "\nQuestion: " + question
    answer = model(prompt, max_length=80)[0]["generated_text"]

    st.session_state.chat.append(("You", question))
    st.session_state.chat.append(("AI", answer))

# show chat
for u, m in st.session_state.chat:
    st.write(f"**{u}:** {m}")
