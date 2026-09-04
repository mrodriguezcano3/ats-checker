import os
import io
import json
from groq import Groq
from PyPDF2 import PdfReader
from typing import Tuple, List
from dotenv import load_dotenv

# Cargar la clave desde el archivo .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extrae el texto crudo de un archivo PDF en memoria."""
    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text

def calculate_match_score(cv_text: str, jd_text: str) -> Tuple[float, List[str]]:
    """Usa Llama 3 vía Groq para calcular la afinidad ultrarrápida."""
    
    prompt = f"""
    You are a strict and analytical Technical Recruiter. Analyze this CV against the Job Offer.
    
    Job Offer:
    {jd_text}
    
    Candidate CV:
    {cv_text}
    
    Instructions:
    1. Extract ALL technical and non-technical requirements from the Job offer (e.g. languages, frameworks, degree, location, methodologies).
    2. Check strictly which of those requirements are explicitly mentioned or clearly implied in the Candidate CV.
    3. Calculate the score.
    
    You MUST return ONLY a valid JSON object with EXACTLY these four keys:
    - "required_skills": <Array of strings with ALL requirements from the offer>
    - "matched_skills": <Array of strings with requirements found in the CV>
    - "missing_skills": <Array of strings with requirements NOT found in the CV>
    - "score": <Float number from 0.0 to 100.0, representing (length of matched_skills / length of required_skills) * 100>
    """ 
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that outputs strictly valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="qwen/qwen3.8-27b", # Modelo muy rápido y eficiente
            temperature=0.1, # Baja temperatura para mayor precisión
            response_format={"type": "json_object"}
        )
        
        # Parseamos el JSON devuelto por Llama 3
        result = json.loads(chat_completion.choices[0].message.content)
        
        # Extraemos de forma segura usando .get()
        score = float(result.get("score", 0.0))
        missing = result.get("missing_skills", [])
        
        return round(score, 1), missing
        
    except Exception as e:
        print(f"Error de IA: {e}")
        return 0.0, ["Error procesando el análisis"]