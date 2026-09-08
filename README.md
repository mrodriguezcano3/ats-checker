## ATS-Checker: AI-Powered Resume Evaluator
An intelligent, full-stack web application designed to evaluate the compatibility between a candidate's resume (PDF) and a job description. Built focusing on modern architectural patterns, clean code, and blazing-fast AI inference.

## Tech Stack & Architecture
* **Frontend:** React, TypeScript, and TailwindCSS v4 bundled with Vite for a responsive, state-driven UI.
* **Backend:** Python and FastAPI providing a robust, asynchronous RESTful API with PyPDF2 for memory-efficient local document parsing.
* **AI Engine:** Integration with Groq API (Qwen 27B model) using Chain of Thought prompting to guarantee precise, structured JSON outputs.
* **Infrastructure:** Docker & Docker Compose configured with multi-stage builds for seamless multi-container orchestration and environment consistency.

## Performance & Metrics
- **Inference Latency:** ~500ms response time for full CV analysis, achieved by leveraging Groq's LPU infrastructure.
- **External Integrations:** 1 (Groq API via HTTP client).
- **Architecture Type:** Stateless REST API with Zero-Shot LLM Inference.
- **Test Coverage:** 56% backend coverage (Pytest & pytest-cov), establishing a solid testing foundation for file validation and schema integrity.

## Core Features
* **Drag & Drop Interface:** Seamless PDF resume uploading with real-time state management and error handling.
* **Contextual AI Analysis:** Utilizes LLMs to understand technologies, synonyms, and implicit requirements rather than relying on rigid, deterministic keyword matching.
* **Actionable Feedback:** Calculates a definitive match score and highlights specific skill gaps (missing technologies) to help candidates improve their profiles.

## How to Run Locally

You will need a free [Groq API Key](https://console.groq.com/keys) to run the AI engine.

### Option 1: Using Docker
You only need Docker and Docker Compose installed on your system.
1. Clone this repository.
2. Navigate to the `/backend` directory and create a `.env` file containing your key: `GROQ_API_KEY=your_key_here`.
3. Open a terminal in the root directory and run:
   ```bash
   docker-compose up --build
4. Open your browser and navigate to http://localhost:3000.

### Option 2: Manual Setup
If you prefer running the services directly on your host machine:

Backend: Navigate to /backend, create and activate a virtual environment (python -m venv venv), run pip install -r requirements.txt, create the .env file with your Groq API key, and start the server with python -m uvicorn app.main:app --reload --port 8000.

Frontend: Open a new terminal in /frontend, run "npm install", and launch the app with "npm run dev".
