from fastapi import APIRouter, Request
from services.ai_service import generate_response

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    response = await generate_response(prompt)
    return {"response": response}