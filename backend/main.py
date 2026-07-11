from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

class InferenceRequest(BaseModel):
    input_text: str
    max_tokens: int = 50
    temperature: float = 1.0
    top_k: int = 50
    top_p: float = 0.9

class InferenceResponse(BaseModel):
    input_text: str
    generated_text: str
    tokens_generated: int

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/inference", response_model=InferenceResponse)
def run_inference(request: InferenceRequest):
    """
    Perform speculative decoding inference using the SSD algorithm.
    """
    try:
        # Call the ML microservice for SSD-based inference
        response = requests.post(
            "http://ml_service:5000/optimize",
            json={
                "input_text": request.input_text,
                "max_tokens": request.max_tokens,
                "temperature": request.temperature,
                "top_k": request.top_k,
                "top_p": request.top_p
            }
        )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        result = response.json()
        return InferenceResponse(
            input_text=result["input_text"],
            generated_text=result["generated_text"],
            tokens_generated=result["tokens_generated"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during inference: {str(e)}")