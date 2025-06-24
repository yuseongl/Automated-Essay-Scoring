import requests
from models import GradingRequest, GradingResponse
from ..config import HUGGINGFACE_API_URL, HUGGINGFACE_TOKEN, OPENAI_API_KEY, USE_PHI4
def grade_essay(request: GradingRequest) -> GradingResponse:
    """
    Grades an essay using a model hosted on Hugging Face or OpenAI.
    
    Args:
        request (GradingRequest): The request containing the essay and grading parameters.
    
    Returns:
        GradingResponse: The response containing the grading results.
    """
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_TOKEN}" if USE_PHI4 else f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": request.essay,
        "parameters": {
            "max_length": 512,
            "do_sample": False
        }
    }
    
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Error from model API: {response.text}")
    
    grading_result = response.json()
    
    return GradingResponse(
        score=grading_result.get("score", 0),
        feedback=grading_result.get("feedback", "")
    )