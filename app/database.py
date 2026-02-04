import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# Why this matters
# -----------------
# engine = connection pool

# SessionLocal = per-request DB session

# Base = parent for all models

# This pattern is everywhere in production FastAPI apps.