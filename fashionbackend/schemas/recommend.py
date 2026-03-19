from pydantic import BaseModel

class RecommendRequest(BaseModel):
    gender: str
    season: str
    occasion: str
    dress_type: str
    budget: float


class RecommendResponse(BaseModel):
    product: list[str]
    shoes: list[str]
    accessory: list[str]
    color: list[str]
