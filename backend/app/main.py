from fastapi import FastAPI
from app.api.v1.router import router as api_router

app = FastAPI(
    title="ATS-Checker API",
    description="API para procesamiento y evaluación de currículums",
    version="0.1.0"
)

# Integración del router bajo un prefijo estándar de la industria
app.include_router(api_router, prefix="/api/v1", tags=["Evaluación"])

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok", "message": "Backend ATS-Checker is running"}