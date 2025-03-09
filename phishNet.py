import streamlit as st
import requests
import time

# Set up page layout and title
st.set_page_config(
    page_title="PhishNet",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="💻",  # Terminal icon
)

# Custom CSS for hacker terminal mode with graphical effects
def hacker_style():
    st.markdown(
        """
        <style>
            /* Hide Streamlit's default header and footer */
            header, footer {visibility: hidden;}

            /* Set the entire app to dark mode */
            .stApp {
                background-color: black !important;
                color: #00ff00 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                overflow: hidden; /* Hide overflow for graphical effects */
            }

            /* Style the toolbar to match the dark theme */
            header[data-testid="stHeader"] {
                background-color: black !important;
                border-bottom: 1px solid #00ff00 !important;
            }

            /* Center the chat box */
            .chat-box {
                border: 2px solid #00ff00;
                padding: 20px;
                background-color: black;
                width: 60%;
                max-width: 600px;
                margin: 0 auto;
                position: relative;
                z-index: 1;
                box-shadow: 0 0 20px #00ff00;
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
                border: 1px solid #00ff00;
                padding: 20px;
                background-color: black;
                white-space: pre-wrap;                max-height: 300px;
                overflow-y: auto;
                margin-bottom: 20px;

                overflow-x: auto;
                width: 100%;
                color: #00ff00;
                font-family: 'Consolas', 'Courier New', monospace;
                box-shadow: 0 0 10px #00ff00;
            }

            /* Center the title */
            .title-container {
                width: 100%;
                margin-bottom: 10px;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
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
        </style>
        """,
        unsafe_allow_html=True,
    )

# Apply the hacker style
hacker_style()

# Graphical effects outside the chat box
st.markdown('<div class="graphics"></div>', unsafe_allow_html=True)

# Display the title and subtitle
st.markdown(
    '<h1 style="font-size: 32px; font-weight: bold; text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00; text-align: center;">💀 PhishNet 💀</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '</div>', unsafe_allow_html=True,
)
st.markdown(
    '<p style="font-size: 16px; color: #00ff00;">Enter a suspicious URL (e.g., \'http://www.goog1e-login.com\') or text (e.g., \'You won a free iPhone! Click here to claim\') to check for phishing threats.</p>',
    unsafe_allow_html=True,
)

# Input field for the user to enter the suspicious text/URL
input_text = st.text_input("💻 Enter suspicious text/URL:")

# Function to analyze phishing using Gemini
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
    - Phishing Risk: [Low/Medium/High]
    - Explanation: [Your explanation here]
    -Confidence: [Number 1-10]
    -Indicators: [List of indicators that led you to the conclusion]
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
        st.warning("⚠️ Enter something to analyze!")
    else:
        with st.spinner("🕵️‍♂️ Scanning for phishing threats..."):
            try:
                # Analyze the input using Gemini
                result = analyze_phishing(input_text)

                # Display the result
                st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
                st.markdown(f"**Analysis Result:**\n\n{result}", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error("❌ Error fetching response! Check your API key or internet connection.")
                st.write(e)
