## ATS-Checker: AI-Powered Resume Evaluator
An intelligent, full-stack web application designed to evaluate the compatibility between a candidate's resume (PDF) and a job description. Built focusing on modern architectural patterns, clean code, and blazing-fast AI inference.

## Tech Stack & Architecture
Frontend: React, TypeScript, and TailwindCSS v4 bundled with Vite for a responsive, state-driven UI.

Backend: Python and FastAPI providing a robust, asynchronous RESTful API with PyPDF2 for memory-efficient local document parsing.

AI Engine: Integration with Groq API (Qwen 27B model) using Chain of Thought prompting to guarantee precise, structured JSON outputs.

## Core Features
Drag & Drop Interface: Seamless PDF resume uploading with real-time state management and error handling.

Contextual AI Analysis: Utilizes LLMs to understand technologies, synonyms, and implicit requirements rather than relying on rigid, deterministic keyword matching.

Actionable Feedback: Calculates a definitive match score and highlights specific skill gaps (missing technologies) to help candidates improve their profiles.

## How to Run Locally
To test this project, you will need Node.js and Python installed, plus a free Groq API Key.

Backend Setup: Navigate to the /backend directory and create a virtual environment (python -m venv venv). Activate it, install dependencies via pip install -r requirements.txt, and create a .env file containing your GROQ_API_KEY. Start the server using python -m uvicorn app.main:app --reload --port 8000.

Frontend Setup: Open a new terminal, navigate to the /frontend directory, run npm install to grab the dependencies, and launch the development server with npm run dev.