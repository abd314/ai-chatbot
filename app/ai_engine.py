import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables (optional if using Docker secrets or platform env vars)
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_response(query: str, model: str = "llama3-8b-8192") -> str:
    """
    Calls Groq Cloud API to generate a response using the specified model.
    Default model: llama3-8b-8192 (fast and free tier eligible)
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        # Fallback or error handling
        raise RuntimeError(f"Groq API error: {str(e)}")