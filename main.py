from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, FlightRecord
from scraper import fetch_flight_data
from chatgpt_client import analyze_trends
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

DATABASE_URL = "sqlite:///./flights.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/flights")
def populate_data():
    data = fetch_flight_data()
    db = SessionLocal()

    for item in data.get("data", []):
        try:
            flight = FlightRecord(
                airline=item["airline"]["name"],
                flight_number=item["flight"]["iata"],
                origin=item["departure"]["iata"],
                destination=item["arrival"]["iata"],
                departure_time=datetime.fromisoformat(item["departure"]["estimated"]),
                price=round(200 + 50 * (item["arrival"].get("delay", 0) or 0), 2)  # Mock pricing
            )
            db.add(flight)
        except Exception:
            continue
    db.commit()
    return {"status": "data loaded"}


from fastapi import Request

@app.post("/insights")
async def get_insights(request: Request):
    flights = await request.json()
    return {"insights": analyze_trends(flights)}


@app.get("/flights")
def get_flights():
    db = SessionLocal()
    flights = db.query(FlightRecord).all()
    db.close()
    return [f.__dict__ for f in flights]   



@app.get("/insights")
def get_insights():
    db = SessionLocal()
    flights = db.query(FlightRecord).all()
    flight_data = [f.__dict__ for f in flights]
    return {"insights": analyze_trends(flight_data)}

@app.get("/flight_count")
def flight_count():
    db = SessionLocal()
    return {"count": db.query(FlightRecord).count()}


from fastapi import Query

@app.get("/filtered_flights")
def get_filtered_flights(
    origin: str = Query(None),
    destination: str = Query(None),
    min_price: float = Query(None),
    max_price: float = Query(None)
):
    db = SessionLocal()
    query = db.query(FlightRecord)

    if origin:
        query = query.filter(FlightRecord.origin == origin)
    if destination:
        query = query.filter(FlightRecord.destination == destination)
    if min_price:
        query = query.filter(FlightRecord.price >= min_price)
    if max_price:
        query = query.filter(FlightRecord.price <= max_price)

    return [f.__dict__ for f in query.all()]


