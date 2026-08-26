const API_URL = 'http://localhost:8000/api/v1';

export const uploadCV = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_URL}/upload-cv`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Error al subir el currículum');
  }

  return response.json();
};

export const analyzeMatch = async (sessionId: string, title: string, description: string) => {
  const response = await fetch(`${API_URL}/session/${sessionId}/analyze`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // Enviamos el JSON estructurado tal como lo espera Pydantic
    body: JSON.stringify({ 
      title: title, 
      description_text: description, 
      required_skills: [] 
    }),
  });

  if (!response.ok) {
    throw new Error('Error al procesar la oferta de trabajo');
  }

  return response.json();
};