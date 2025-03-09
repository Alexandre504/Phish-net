# Phish-Net 🐟🕸️  

Phish-Net is a powerful phishing detection tool that helps users identify potential phishing attempts in URLs and text. Designed with a hacker-themed interface, it provides a sleek and intuitive experience while leveraging AI to analyze threats effectively.  

---

## Features 🚀  
✔ **Hacker-Themed UI** – A dark terminal-style interface with green text, animations, and effects.  
✔ **AI-Powered Analysis** – Uses Google Gemini to detect phishing risks in real-time.  
✔ **Easy to Use** – Simply enter a URL or text, and get an instant risk assessment.  
✔ **Privacy Focused** – No data is stored or shared; everything is analyzed in real-time.  

---

## How to Use 🛠️  

1. **Run the App**  
   - Install dependencies:  
     ```bash
     pip install streamlit requests
     ```
   - Run the app:  
     ```bash
     streamlit run app.py
     ```  

2. **Enter a Suspicious URL or Text**  
   - Type a URL or text into the input box.  

3. **Analyze for Phishing**  
   - Click the "🔍 Analyze" button to check for phishing risks.  

4. **View Results**  
   - The tool will display a phishing risk level (**Low/Medium/High**) along with an explanation.  

---

## Installation 📥  

Make sure you have Python installed. Then, clone the repository and install the required packages:  

```bash
git clone https://github.com/your-repo/phish-net.git
cd phish-net
pip install -r requirements.txt
```

---

## API Key Setup 🔑  

Phish-Net uses Google Gemini for phishing analysis. Replace `API_KEY` in `app.py` with your own key:  

```python
API_KEY = "your_gemini_api_key_here"
```

---

## Privacy Policy 🔒  

- **No data is stored** – All analysis happens in real-time.  
- **No user tracking** – Your inputs are not logged or saved.  

---

## About ℹ️  

Phish-Net is designed to help users stay safe online by detecting phishing attempts in emails, links, and messages. With a stylish hacker-themed interface, it makes cybersecurity engaging and accessible.  

Developed by: **[alex, aron, jake and ali]**  
GitHub: **[]**  

Stay safe from phishing attacks! 🕵️‍♂️💻
