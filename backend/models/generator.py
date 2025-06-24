from pydantic import BaseModel
from typing import Optional, List

class GenerationRequest(BaseModel):
    """Request model for generating an essay.
    """
    topic: str
    length: int  # Desired length of the essay in words
    style: Optional[str] = None  # Optional style or tone for the essay
    difficulty: str  # Difficulty level of the essay (e.g., "easy", "medium", "hard")
    parameters: Optional[dict] = None  # Additional parameters for generation, if any
    
    
class GenerationResponse(BaseModel):
    """Response model for the generated essay.
    """
    question: str  # The generated essay text
    topic: str  # The topic of the essay
    length: int  # Length of the generated essay in words
    style: Optional[str] = None  # Style or tone used for the generation, if specified
    parameters: Optional[dict] = None  # Parameters used for generation, if any 
    

