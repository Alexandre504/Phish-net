import streamlit as st
import requests

# Set up page layout and title
st.set_page_config(
    page_title="Phish-Net",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="🐟",  # Fish icon
)

# Custom CSS for a clean and professional hacker terminal mode
def hacker_style():
    st.markdown(
        """
        <style>
            /* Set the entire app to dark mode */
            .stApp {
                background-color: black !important;
                color: #00ff00 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                overflow: hidden; /* Hide overflow for graphical effects */
                text-align: center; /* Center all text */
            }

            /* Style the toolbar to match the dark theme */
            header[data-testid="stHeader"] {
                background-color: black !important;
                border-bottom: 1px solid #00ff00 !important;
            }

            /* Add fish and net emoji to the top-left corner of the toolbar */
            header[data-testid="stHeader"]::before {
                content: "🐟🕸️";
                font-size: 24px;
                margin-right: 10px;
                position: absolute;
                left: 10px;
                top: 50%;
                transform: translateY(-50%);
            }

            /* Style the input fields */
            .stTextInput>div>div>input {
                background-color: black !important;
                color: #00ff00 !important;
                border: 1px solid #00ff00 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                padding: 10px;
                width: 100%;
                margin-bottom: 20px;
            }

            /* Style the input label */
            .stTextInput>label {
                color: #00ff00 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
            }

            /* Style the buttons */
            .stButton>button {
                background-color: black !important;
                color: #00ff00 !important;
                border: 1px solid #00ff00 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                padding: 10px;
                width: 100%;
                margin-bottom: 20px;
                transition: all 0.3s ease;
            }

            /* Hover effect for buttons */
            .stButton>button:hover {
                background-color: #00ff00 !important;
                color: black !important;
                border: 1px solid #00ff00 !important;
                transform: scale(1.05);
                box-shadow: 0 0 10px #00ff00;
            }

            /* Style the terminal output box */
            .terminal-box {
                border: 1px solid #00ff00; /* Thin border */
                padding: 20px;
                background-color: black;
                white-space: pre-wrap;
                overflow-x: auto;
                width: 100%;
                color: #00ff00;
                font-family: 'Consolas', 'Courier New', monospace;
                box-shadow: 0 0 10px #00ff00;
                margin: 20px auto;
            }

            /* Style the spinner */
            .stSpinner>div {
                color: #00ff00 !important;
            }

            /* Style warnings and errors */
            .stWarning, .stError {
                font-family: 'Consolas', 'Courier New', monospace !important;
                color: #ff0000 !important;
                text-align: center;
                margin: 20px auto;
                width: 80%;
                max-width: 800px;
            }

            /* Add a blinking cursor effect */
            @keyframes blink {
                0% { opacity: 1; }
                50% { opacity: 0; }
                100% { opacity: 1; }
            }

            .blinking-cursor {
                display: inline-block;
                width: 10px;
                height: 20px;
                background-color: #00ff00;
                animation: blink 1s infinite;
            }

            /* Graphical effects outside the chat box */
            .graphics {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 0;
            }

            .graphics::before, .graphics::after {
                content: "";
                position: absolute;
                background: radial-gradient(circle, #00ff00 10%, transparent 10.01%);
                opacity: 0.2;
                animation: moveParticles 10s linear infinite;
            }

            .graphics::before {
                top: 20%;
                left: 10%;
                width: 100px;
                height: 100px;
                animation-duration: 15s;
            }

            .graphics::after {
                top: 50%;
                left: 80%;
                width: 150px;
                height: 150px;
                animation-duration: 20s;
            }

            @keyframes moveParticles {
                0% { transform: translateY(0) translateX(0); }
                50% { transform: translateY(100px) translateX(100px); }
                100% { transform: translateY(0) translateX(0); }
            }

            /* Style for the big title box */
            .title-box {
                border-bottom: 1px solid #00ff00; /* Thin line */
                padding: 10px;
                background-color: black;
                width: 50%;
                max-width: 500px;
                margin: 0 auto 20px auto;
                text-align: center;
                font-size: 28px;
                font-weight: bold;
                color: #00ff00;
            }

            /* Style for the bottom sections */
            .bottom-section {
                margin-top: 40px;
                text-align: center;
            }

            .bottom-section button {
                background-color: black !important;
                color: #00ff00 !important;
                border: 1px solid #00ff00 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                padding: 10px 20px;
                margin: 5px;
                transition: all 0.3s ease;
            }

            .bottom-section button:hover {
                background-color: #00ff00 !important;
                color: black !important;
                border: 1px solid #00ff00 !important;
                transform: scale(1.05);
                box-shadow: 0 0 10px #00ff00;
            }

            /* Style for the lines */
            .line {
                border-bottom: 1px solid #00ff00;
                width: 80%;
                margin: 20px auto;
                box-shadow: 0 0 10px #00ff00;
            }

            /* Style for the binary text */
            .binary-text {
                position: fixed;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                color: #00ff00;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 12px;
                opacity: 0.7;
                text-shadow: 0 0 5px #00ff00;
            }

            /* Style for shiny green text */
            .shiny-green {
                color: #00ff00 !important;
                text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Apply the hacker style
hacker_style()

# Graphical effects outside the chat box
st.markdown('<div class="graphics"></div>', unsafe_allow_html=True)

# Display the big title box with net and fish logo
st.markdown(
    '<div class="title-box">🐟 Phish-Net 🕸️</div>',
    unsafe_allow_html=True,
)

# Introduction text
introduction = """
Welcome to Phish-Net! I am here to help you detect phishing threats. 
Phishing attempts often try to steal personal information, such as passwords, 
credit card numbers, or other sensitive data. Enter a suspicious URL or text 
below to get started.
"""

# Display the introduction
st.markdown(f"<p style='color: #00ff00; text-align: center;'>{introduction}</p>", unsafe_allow_html=True)

# Input field for the user to enter the suspicious text/URL
input_text = st.text_input("💻 Enter suspicious text/URL:")

# Function to analyze phishing using Google Gemini
def analyze_phishing(input_text):
    """
    Analyze the input text/URL for phishing using Google Gemini.
    """
    API_KEY = "AIzaSyDRECj0dxtg9HltTS5GgQBbwaVrRq1OUwg"  # Replace with your Gemini API key
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    # Craft a prompt to detect phishing
    prompt = f"""
    Analyze the following text or URL and determine if it is a phishing attempt. 
    Phishing attempts often try to steal personal information, such as passwords, credit card numbers, or other sensitive data.
    Look for signs like suspicious domains, urgent language, or requests for personal information.

    Input: {input_text}

    Provide your analysis in the following format:
    Phishing Risk: [Low/Medium/High]
    Explanation: [Your explanation here]
    """

    # Send the prompt to Gemini
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        json={"contents": [{"parts": [{"text": prompt}]}]},
    )

    if response.status_code == 200:
        data = response.json()
        if "candidates" in data and data["candidates"]:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Error: No response from Gemini."
    else:
        return f"Error: {response.status_code} - {response.text}"

# When the button is pressed, analyze the input
if st.button("🔍 Analyze"):
    if not input_text.strip():
        # Replace the empty box with a line
        st.markdown('<div class="line"></div>', unsafe_allow_html=True)
    else:
        with st.spinner("🕵️‍♂️ Scanning for phishing threats..."):
            try:
                # Analyze the input using Gemini
                result = analyze_phishing(input_text)

                # Format the result
                result = result.replace("- ", "")  # Remove the dots
                result = result.replace("Phishing Risk:", "<span class='shiny-green'>Phishing Risk:</span>   ")  # Add 3 spaces
                result = result.replace("Explanation:", "<span class='shiny-green'>Explanation:</span>   ")  # Add 3 spaces

                # Display the result
                st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
                st.markdown(f"**{result}**", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error("❌ Error fetching response! Check your API key or internet connection.")
                st.write(e)

# Bottom sections for About and Privacy Policy
st.markdown('<div class="bottom-section">', unsafe_allow_html=True)

# Toggle buttons for About and Privacy Policy
col1, col2 = st.columns(2)
with col1:
    if st.button("About"):
        st.session_state.show_about = True
        st.session_state.show_privacy = False
with col2:
    if st.button("Privacy Policy"):
        st.session_state.show_privacy = True
        st.session_state.show_about = False

# Display About or Privacy Policy content
if st.session_state.get("show_about"):
    st.markdown('<div class="line"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        **About Phish-Net**  
        Phish-Net is a powerful tool designed to detect phishing threats in URLs and text. 
        It uses advanced AI models to analyze and identify potential phishing attempts, helping you stay safe online.
        """,
        unsafe_allow_html=True,
    )

if st.session_state.get("show_privacy"):
    st.markdown('<div class="line"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        **Privacy Policy**  
        Your privacy is important to us. Phish-Net does not store or share any data you input. 
        All analyses are performed in real-time, and no information is retained after the session ends.
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# Display binary names at the bottom
st.markdown(
    '<div class="binary-text">01000001 01110010 01101111 01101110 | 01000001 01101100 01101001 | 01000001 01101100 01100101 01111000 | 01001010 01100001 01101011 01100101</div>',
    unsafe_allow_html=True,
)
