import os
from groq import Groq
from dotenv import load_dotenv

# Carga tu API Key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Consulta los modelos activos directamente a los servidores de Groq
print("Modelos disponibles actualmente en Groq:\n")
try:
    models = client.models.list()
    for model in models.data:
        print(f"- {model.id}")
except Exception as e:
    print(f"Error al consultar la API: {e}")