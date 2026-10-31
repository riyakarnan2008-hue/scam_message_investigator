# Scam Message Investigator

## Project Description
Scam Message Investigator is an AI-powered application that detects suspicious and fraudulent SMS messages using the Gemma 3 (1B) Large Language Model through Ollama. The application is developed using Python and Streamlit.

## Objectives
- Identify scam and suspicious SMS messages.
- Analyze message content using AI.
- Classify messages as Scam, Legitimate, or Suspicious.
- Display risk levels.
- Provide warning signs and safety advice.

## Technologies Used
- Python
- Streamlit
- Ollama
- Gemma 3 (1B)
- VS Code

## Features
- SMS message input.
- AI-powered scam detection.
- Scam classification.
- Risk level identification.
- Warning signs analysis.
- Safety recommendations.

## Project Structure
```text
scam message investigator/
│
├── app.py
├── llm.py
├── test.py
└── README.md
```

## Installation

### 1. Install Ollama
Download Ollama from:
https://ollama.com/

### 2. Download Gemma Model
```bash
ollama pull gemma3:1b
```

### 3. Install Required Libraries
```bash
pip install streamlit ollama
```

## Run the Application

```bash
python -m streamlit run app.py
```

Open in your browser:

http://localhost:8501

## How It Works
1. Enter an SMS message into the application.
2. Click the Analyze button.
3. Gemma 3 (1B) processes the message.
4. The application displays the classification and risk level.
5. The user receives warning signs and safety advice.

## Expected Output
- Classification: Scam / Legitimate / Suspicious
- Risk Level: High / Medium / Low
- Reason
- Warning Signs
- Safety Advice

## Disclaimer
This application is developed for educational purposes. AI predictions are not guaranteed to be accurate. Always verify suspicious messages through official channels before taking action.

## Conclusion
Scam Message Investigator uses a locally running AI model to help identify suspicious SMS messages and improve awareness of common online scams.
