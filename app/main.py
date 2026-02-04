from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import SessionLocal, engine
import models


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/locations")
def create_location(
    name: str,
    latitude: float,
    longitude: float,
    db: Session = Depends(get_db)
):
    location = models.Location(
        name=name,
        latitude=latitude,
        longitude=longitude
    )
    db.add(location)
    db.commit()
    db.refresh(location)
    return location

@app.get("/locations")
def get_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return JSONResponse(status_code=200, content={"status": "healthy"})
    except Exception as e:
        return JSONResponse(status_code=503, content={"status": "unhealthy", 
                                                      "database": "unreachable",
                                                       "error": str(e)})
    
# Why this works (important explanation)

# Depends(get_db)

# Reuses your existing DB session logic

# No duplicate connection code

# SELECT 1

# Lightweight

# No table dependency

# Industry-standard health probe

# 503

# Signals infra-level failure

# Load balancers understand this