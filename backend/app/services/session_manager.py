from uuid import uuid4
from typing import Dict
from app.models.schemas import EvaluationSession

# Diccionario global para simular almacenamiento en memoria (como Redis)
_sessions: Dict[str, EvaluationSession] = {}

def create_session() -> EvaluationSession:
    """Genera una nueva sesión con un UUID único."""
    session_id = str(uuid4())
    new_session = EvaluationSession(session_id=session_id)
    _sessions[session_id] = new_session
    return new_session

def get_session(session_id: str) -> EvaluationSession:
    """Recupera una sesión existente."""
    return _sessions.get(session_id)