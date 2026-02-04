from sqlalchemy import Column, Integer, String, Float, Index
from database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    __table_args__ = (
        Index("idx_location_lat_lon", "latitude", "longitude"),
    )


# Why these choices

# Float

# Fine for MVP geo work

# Simple and widely supported

# nullable=False

# Enforces data integrity

# Composite index (latitude, longitude)

# Enables fast bounding-box queries later

# Shows you think about performance

# This is very interview-friendly.