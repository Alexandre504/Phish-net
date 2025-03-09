import requests

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