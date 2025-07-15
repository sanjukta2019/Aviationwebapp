# Aviationwebapp
 Python Web App for Airline Booking Market Demand Data
Airline Booking Insights Dashboard
A dynamic, AI-powered dashboard built with FastAPI, Bootstrap, and Chart.js that analyzes flight booking trends, pricing, and routes. Designed for both technical and non-technical users to explore flight data with ease. 
Features:
Filter flights by origin, destination, and price range
Get AI-generated summaries for filtered flight data
Populate flights dynamically via AviationStack API
Easy deployment-ready backend with FastAPI
Built-in SQLite database with ORM modeling via SQLAlchemy

    Project Structure

    ├── main.py               # FastAPI server with routes
    ├── models.py             # SQLAlchemy models
    ├── scraper.py            # Flight data fetcher
    ├── chatgpt_client.py     # AI-powered summary logic
    ├── templates/
    │   └── index.html        # Frontend dashboard
    ├── static/               # Optional JS/CSS files
    ├── flights.db            # SQLite database (created on runtime)
    ├── requirements.txt      # Project dependencies
    ├── .env                  # Environment variables (not committed)
    └── README.md             # Project overview



    Setup Instructions
    1. Create Virtual Environment
    python -m venv myenv
    2. Activate
    myenv\Scripts\activate

    3. Install Dependencies
    pip install -r requirements.txt

    4. Create .env file and put your api key details
    AVIATIONSTACK_API_KEY=your_aviationstack_api_key
    AIPIPE_TOKEN=your_aipipe_api_token

    5. Run the app
    uvicorn main:app --reload
    6. May run the command in bash to load the flights data
    curl -X POST http://localhost:8000/flights





