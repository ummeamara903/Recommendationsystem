from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.recommend import RecommendRequest
from models.recommend import Recommendation
from services.recommendServices import recommend

router = APIRouter()

@router.post("/recommend")
def get_recommendation(
    data: RecommendRequest,
    db: Session = Depends(get_db)
):
    
    result = recommend(data)

    # Save to DB
    record = Recommendation(
        gender=data.gender,
        season=data.season,
        occasion=data.occasion,
        dress_type=data.dress_type,
        budget=data.budget,
        product=",".join(result["product"]),
        shoes=",".join(result["shoes"]),
        accessory=",".join(result["accessory"]),
        color=",".join(result["color"])
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return result
