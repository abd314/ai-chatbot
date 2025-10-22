from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.cache import RedisCache
from app.ai_engine import generate_ai_response
import os

app = FastAPI(title="AI Chatbot with Groq + Redis")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_TTL = int(os.getenv("CACHE_TTL", 600))  # 10 minutes

cache = RedisCache(host=REDIS_HOST, port=REDIS_PORT, ttl=CACHE_TTL)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    query: str
    response: str
    cached: bool

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    # Check cache
    cached_response = cache.get(query)
    if cached_response is not None:
        return ChatResponse(
            query=query,
            response=cached_response,
            cached=True
        )

    # Call Groq API
    try:
        ai_response = generate_ai_response(query)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    # Cache and return
    cache.set(query, ai_response)

    return ChatResponse(
        query=query,
        response=ai_response,
        cached=False
    )