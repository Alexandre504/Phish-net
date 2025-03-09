import streamlit as st
from phishing_analyzer import analyze_phishing

# Set up page layout and title
st.set_page_config(
    page_title="Phish-Net",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="🐟",  # Fish icon
)

# Custom CSS for a clean and professional hacker terminal mode
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
                # Display the result
                st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
                st.markdown(f"**Analysis Result:**\n\n{result}", unsafe_allow_html=True)
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
    '<div class="binary-text">01000001 01100001 01110010 01101111 01101110 | 01000001 01101100 01101001 | 01000001 01101100 01100101 01111000 | 01001010 01100001 01101011 01100101</div>',
    unsafe_allow_html=True,
)
