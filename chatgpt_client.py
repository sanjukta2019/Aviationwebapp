from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AIPIPE_TOKEN"),
    base_url="https://aipipe.org/openai/v1"
)

def analyze_trends(flight_data):
    prompt = f"""
    Analyze the following airline booking data and summarize:
    - Demand trends
    - Pricing changes
    - Popular routes

    Data: {flight_data}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a travel data analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content

    except Exception as e:
        print("❌ AI Pipe error:", e)
        return "AI analysis failed."
