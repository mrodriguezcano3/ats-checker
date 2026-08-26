import io
import re
from PyPDF2 import PdfReader
from typing import Tuple, List

# Diccionario de habilidades técnicas para el alcance de la demo.
# En un entorno real, esto vendría de una base de datos o un modelo de IA entrenado.
TECH_DICTIONARY = {
    "python", "java", "javascript", "typescript", "c++", "c#", ".net", "php", "ruby",
    "react", "angular", "vue", "svelte", "html", "css", "tailwind", "bootstrap",
    "node", "express", "fastapi", "django", "spring", "flask",
    "sql", "mysql", "postgresql", "mongodb", "redis", "nosql",
    "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins", "github actions",
    "git", "github", "gitlab", "agile", "scrum", "graphql", "rest", "api"
}

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extrae el texto crudo de un archivo PDF en memoria."""
    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text.lower()

def extract_skills(text: str) -> set:
    """Encuentra qué habilidades del diccionario están presentes en el texto."""
    # Usamos expresiones regulares para extraer palabras limpias (incluyendo símbolos como c++ o .net)
    words = re.findall(r'\b[a-z0-9+#.-]+\b', text.lower())
    
    # Encontramos la intersección entre las palabras del texto y nuestro diccionario
    found_skills = set(words).intersection(TECH_DICTIONARY)
    
    # Manejo de casos especiales para frases compuestas (ej. "github actions")
    if "github" in text.lower() and "actions" in text.lower():
        found_skills.add("github actions")
        
    return found_skills

def calculate_match_score(cv_text: str, jd_text: str) -> Tuple[float, List[str]]:
    """Compara las habilidades del CV contra las de la oferta de trabajo."""
    cv_skills = extract_skills(cv_text)
    jd_skills = extract_skills(jd_text)
    
    # Si la oferta no menciona ninguna tecnología de nuestro diccionario
    if not jd_skills:
        return 0.0, []
        
    # Calculamos qué habilidades de la oferta están en el CV
    matched_skills = cv_skills.intersection(jd_skills)
    missing_skills = jd_skills - cv_skills
    
    # Fórmula del score: (Habilidades coincidentes / Total habilidades solicitadas) * 100
    score = (len(matched_skills) / len(jd_skills)) * 100
    
    # Devolvemos el score redondeado a 1 decimal y la lista de lo que falta
    return round(score, 1), list(missing_skills)