from fastapi import FastAPI
from api import grader, generator
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Automated Essay Scoring & generation question API",
    description="API for scoring essays using my LLM models. And generating questions based on the essay.",
    version="1.0.0",
)

app.include_router(grader.router, prefix="/api/grader", tags=["Grader"])
app.include_router(generator.router, prefix="/api/genrator", tags=["Generator"])