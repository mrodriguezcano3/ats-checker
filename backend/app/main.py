from fastapi import FastAPI

app = FastAPI(
    title="ATS-Checker API",
    description="API para procesamiento y evaluación de currículums",
    version="0.1.0"
)

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok", "message": "Backend ATS-Checker is running"}