import os
import openai

from fastapi import APIRouter
from models.generator import GenerationRequest, GenerationResponse
from services.generator.gpt import gpt_generator
from config import OPEN_AI_API_KEY
from openai import AsyncOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()
client = AsyncOpenAI(api_key=OPEN_AI_API_KEY)

@router.post("/generate", response_model=GenerationResponse)
async def gen_question_endpoint(request: GenerationRequest) -> GenerationResponse:
    """
    Generates an question based on the provided topic and parameters.
    
    Args:
        request (GenerationRequest): The request containing the topic, length, style, and parameters for generation.
    
    Returns:
        GenerationResponse: The response containing the generated question and its details.
    """
    question = await gpt_generator(request)
    
    return GenerationResponse(
        question=question,
        topic=request.topic,
        length=request.length,
        style=request.style,
        parameters=request.parameters
    )
    