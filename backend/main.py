from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/inference")
def run_inference(payload: dict):
    # Placeholder for SSD-based inference logic
    return {"message": "Inference result placeholder"}
