# Task 2: Upload a CSV file via Streamlit and display summary statistics.

import streamlit as st
import pandas as pd

# App title
st.title("📊 CSV Data Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Show dataset
    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

    # Show summary statistics
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())
else:
    st.info("Please upload a CSV file to see the analysis")
