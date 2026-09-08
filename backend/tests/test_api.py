from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_upload_invalid_file_format():
    """Verifica que el endpoint rechaza de forma segura los archivos que no son PDF."""
    
    fake_file = io.BytesIO(b"Este es un CV falso en formato texto")
    
    response = client.post(
        "/api/v1/upload-cv",
        files={"file": ("cv.txt", fake_file, "text/plain")}
    )
    
    assert response.status_code == 400
    assert "PDF" in response.json()["detail"]