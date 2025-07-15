from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_flight_data():
    params = {
        "access_key": API_KEY,
        "limit": 100
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
