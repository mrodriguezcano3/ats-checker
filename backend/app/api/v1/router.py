from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import session_manager
from app.models.schemas import EvaluationSession
from app.models.schemas import EvaluationSession, JobOffer
from app.services import session_manager, nlp_engine
from app.models.schemas import EvaluationSession, JobOffer, CandidateProfile

router = APIRouter()

@router.post("/upload-cv", response_model=EvaluationSession)
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF.")
    
    session = session_manager.create_session()
    
    # Leemos el archivo en memoria y extraemos el texto usando el NLP Engine
    content = await file.read()
    extracted_text = nlp_engine.extract_text_from_pdf(content)
    
    # Guardamos el texto extraído en el modelo del candidato dentro de la sesión
    session.candidate = CandidateProfile(raw_text=extracted_text)
    session.status = "processing"
    
    return session

@router.get("/session/{session_id}", response_model=EvaluationSession)
async def get_session_status(session_id: str):
    """Devuelve el estado actual y los resultados de una sesión de evaluación."""
    session = session_manager.get_session(session_id)
    
    if not session:
        raise HTTPException(status_code=404, detail="Sesión no encontrada o expirada")
        
    return session

@router.post("/session/{session_id}/analyze", response_model=EvaluationSession)
async def analyze_match(session_id: str, job_offer: JobOffer):
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Sesión no encontrada o expirada")
    
    session.job_offer = job_offer
    
    # Verificamos que tengamos el texto del CV
    if not session.candidate or not session.candidate.raw_text:
        raise HTTPException(status_code=400, detail="No hay datos del currículum en esta sesión.")
    
    #  EJECUCIÓN DEL ALGORITMO REAL
    score, missing = nlp_engine.calculate_match_score(
        cv_text=session.candidate.raw_text,
        jd_text=job_offer.description_text
    )
    
    session.status = "completed"
    session.match_percentage = score
    session.missing_skills = missing
    
    return session   