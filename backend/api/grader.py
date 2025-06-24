from fastapi import APIRouter
from models.grader import GrandeResponse, GrandeRequest
from services.grader import grade_essay

router = APIRouter()

@router.post("/grade", response_model=GrandeResponse)
async def grade_essay_endpoint(request: GrandeRequest):
    """
    Endpoint to grade an essay.
    """
    return await grade_essay(request)