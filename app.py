app.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_incident(incident):

    prompt = f'''
    Analyze telecom incident and provide:
    1. Summary
    2. Root Cause
    3. Recommendations
    4. Escalation Advice

    Incident:
    {incident}
    '''

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are telecom AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response["choices"][0]["message"]["content"]

sample_incident = '''
Customer internet outage in Mumbai.
BGP peer flapping detected.
'''

print(analyze_incident(sample_incident))
