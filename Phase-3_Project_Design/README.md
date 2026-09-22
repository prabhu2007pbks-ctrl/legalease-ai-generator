# Phase 3: Project Design Phase

## Architecture Diagram Overview
1. User interacts with Streamlit Web UI.
2. User selects document type and inputs details & API Key.
3. Streamlit app sends prompt request to Google Gemini API (gemini-2.5-flash).
4. Gemini API processes and returns generated legal text.
5. Streamlit app displays output on screen for preview/copying.

## UI/UX Design
- Sidebar: Gemini API Key Input.
- Main Page: Selectbox for document type, Text Area for input parameters, Generate Button, and Output Text Box.
