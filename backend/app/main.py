from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router as api_router

app = FastAPI(
    title="ATS-Checker API",
    description="API para procesamiento y evaluación de currículums",
    version="0.1.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # El puerto de tu frontend (React/Vite)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1", tags=["Evaluación"])

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok", "message": "Backend ATS-Checker is running"}