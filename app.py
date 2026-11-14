
import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Tavily Research Agent",
    page_icon="🔍",
    layout="wide"
)

# APPLICATION HEADER
st.title("🔍 Tavily Research Agent")

st.markdown(
    "### AI-Powered Web Research and Report Generator"
)

st.write(
    "Enter a research topic and let AI investigate it, "
    "analyse evidence, and generate a research report."
)

st.divider()

# USER INPUT
topic = st.text_area(
    "Enter your research topic:",
    placeholder="Example: Latest developments in Artificial Intelligence"
)

research_depth = st.selectbox(
    "Select Research Depth:",
    ["Quick", "Standard", "Detailed"]
)

# START BUTTON
if st.button("🚀 Start Research", type="primary"):

    if not topic.strip():
        st.warning("Please enter a research topic.")

    else:
        st.info(
            "Your research topic has been received. "
            "The AI research engine will be connected in the next step."
        )
