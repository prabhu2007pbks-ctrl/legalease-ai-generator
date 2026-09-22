
import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(page_title="Legal Ease - AI Legal Document Generator", page_icon="⚖️", layout="wide")

st.title("⚖️ Legal Ease: AI-Powered Legal Document Generator")
st.write("Generate professional legal documents easily using Google Gemini API.")

# Sidebar for API Key
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Google Gemini API Key:", type="password")

# Main Interface
doc_type = st.selectbox(
    "Select Document Type:",
    ["Rental Agreement", "Non-Disclosure Agreement (NDA)", "Affidavit", "General Contract"]
)

st.subheader("Document Details")
user_input = st.text_area(
    "Enter the relevant details (e.g., Names of parties, terms, duration, amounts, location):",
    height=150,
    placeholder="e.g., Landlord: Ramesh, Tenant: Suresh, Monthly Rent: ₹15,000, Duration: 11 months, Location: Chennai..."
)

if st.button("Generate Legal Document"):
    if not api_key:
        st.error("Please enter your Google Gemini API Key in the sidebar.")
    elif not user_input:
        st.warning("Please provide details for the document.")
    else:
        with st.spinner("Generating legal document..."):
            try:
                # Initialize Gemini Client
                client = genai.Client(api_key=api_key)
                
                # Construct Prompt
                prompt = f"""
                You are an expert legal draft assistant.
                Generate a formal and legally sound draft for a {doc_type} based on the following details:
                
                {user_input}
                
                Please ensure the document includes standard legal clauses, clear headings, and placeholders for signatures.
                """
                
                # Call Gemini API
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                st.success("Document Generated Successfully!")
                st.subheader("Generated Draft")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
