import streamlit as st

st.title("Hello Streamlit 👋")
st.write("My first Streamlit app running in VS Code")

user_input = st.text_input("Enter text")
if st.button("Submit"):
    result = user_input.upper()
    st.write(result)

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Add"):
    st.session_state.count += 1

st.write(st.session_state.count)
