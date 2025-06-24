from pydantic import BaseModel, Field
from typing import Optional

class Grader(BaseModel):
    """
    Grader model for storing grading information.
    """
    id: Optional[int] = None
    essay_id: int
    score: float
    feedback: str
    grader_name: str
    timestamp: str
    
class GrandeRequest(BaseModel):
    """
    Request model for grading an essay.
    """
    institution:str = Field(..., alias='기관')
    writing: str = Field(..., alias='작문')
    prompt: str = Field(..., alias='발문')
    options: str = Field(..., alias='보기')
    score_assignment: int = Field(..., alias='배점_과제')
    score_language: int = Field(..., alias='배점_언어')
    score_contents: int = Field(..., alias='배점_내용')
    score_useage: int = Field(..., alias='배점_사용법')
    score_logic: int = Field(..., alias='배점_논리')
    min_length: int = Field(..., alias='최소 길이')
    max_length: int = Field(..., alias='최대 길이')
    question_number: int = Field(..., alias='문항번호')

class GrandeResponse(BaseModel):
    """
    Response model for the grading result.
    """
    assignment:int = Field(..., description="과제")
    language:int = Field(..., description="언어")
    content:int = Field(..., description="내용")
    useage:int = Field(..., description="사용법")
    logic:int = Field(..., description="논리")

    probability_assignment:float = Field(..., description="과제_확률")
    probability_language:float = Field(..., description="언어_확률")
    probability_content:float = Field(..., description="내용_확률")
    probability_useage:float = Field(..., description="사용법_확률")
    probability_logic:float = Field(..., description="논리_확률")
    message: str = Field(..., description="메시지")