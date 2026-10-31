
import ollama

def investigate_message(message):
    prompt = f"""
You are a Scam Message Investigator.

Analyze this message carefully:

"{message}"

Return your analysis using this format:

1. Classification: Scam / Legitimate / Suspicious
2. Risk Level: High / Medium / Low
3. Warning Signs: List the suspicious words or patterns.
4. Analysis: Explain why the message is suspicious or legitimate.
5. Safety Advice: Explain what the receiver should do.

IMPORTANT:
- Analyze the actual message.
- Do not give only a disclaimer.
- Do not ask the user whether they want another analysis.
- Give a clear and direct answer.
- If evidence is insufficient, say so.

"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
