from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from data import FAQ
from chatbot import get_gemini_response
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve HTML templates
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(data: Message):
    user_msg = data.message.strip()
    if user_msg in FAQ:
        return {"response": FAQ[user_msg]}
    return {"response": get_gemini_response(user_msg)}
