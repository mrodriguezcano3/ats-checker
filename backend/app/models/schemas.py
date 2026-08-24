from pydantic import BaseModel, Field
from typing import List, Optional

# 1. Datos de la oferta de trabajo
class JobOffer(BaseModel):
    title: str
    required_skills: List[str] = []
    description_text: str

# 2. Datos extraídos del CV
class CandidateProfile(BaseModel):
    raw_text: str = ""
    detected_skills: List[str] = []
    experience_years: Optional[int] = 0

# 3. Documento principal (El Value de nuestra Key en Redis/Memoria)
class EvaluationSession(BaseModel):
    session_id: str = Field(..., description="UUID único de la sesión")
    status: str = Field(default="pending", description="pending, processing, completed, error")
    match_percentage: float = 0.0
    missing_skills: List[str] = []
    job_offer: Optional[JobOffer] = None
    candidate: Optional[CandidateProfile] = None