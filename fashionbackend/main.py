from fastapi import FastAPI
from core.database import Base, engine
from api.recommend import router as recommend_router

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(recommend_router, prefix="/api", tags=["Recommendation"])
