from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import session_manager
from app.models.schemas import EvaluationSession

router = APIRouter()

@router.post("/upload-cv", response_model=EvaluationSession)
async def upload_resume(file: UploadFile = File(...)):
    """Recibe un PDF, crea una sesión y devuelve el UUID."""
    
    # 1. Validación temprana
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF.")
    
    # 2. Inicializar la sesión
    session = session_manager.create_session()
    
    # 3. Leer el archivo (por ahora solo validamos que llega el contenido)
    content = await file.read()
    
    # Simulamos que pasamos el contenido a estado de procesamiento
    session.status = "processing"
    
    return session

@router.get("/session/{session_id}", response_model=EvaluationSession)
async def get_session_status(session_id: str):
    """Devuelve el estado actual y los resultados de una sesión de evaluación."""
    session = session_manager.get_session(session_id)
    
    if not session:
        raise HTTPException(status_code=404, detail="Sesión no encontrada o expirada")
        
    return session