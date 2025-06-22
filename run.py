from fastapi import FastAPI
from api import scoreing
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router()