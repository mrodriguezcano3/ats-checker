import { useState } from 'react';
import FileUploader from './components/FileUploader';
import JobOfferForm from './components/JobOfferForm';

function App() {
  // Estado global de la aplicación
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [result, setResult] = useState<any | null>(null);

  // Función para reiniciar el flujo
  const handleRestart = () => {
    setSessionId(null);
    setResult(null);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
      <header className="mb-12 text-center">
        <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight mb-2">
          ATS<span className="text-blue-600">-Checker</span>
        </h1>
        <p className="text-gray-600 text-lg">
          Evalúa la afinidad de tu currículum al instante
        </p>
      </header>

      <main className="w-full max-w-3xl">
        
        {/* PASO 1: Subida de CV (Se muestra si no hay ID de sesión) */}
        {!sessionId && (
          <FileUploader onUploadSuccess={(id) => setSessionId(id)} />
        )}

        {/* PASO 2: Formulario de Oferta (Se muestra si hay sesión pero no hay resultados) */}
        {sessionId && !result && (
          <JobOfferForm 
            sessionId={sessionId} 
            onAnalysisComplete={(data) => setResult(data)} 
          />
        )}

        {/* PASO 3: Resultados (Se muestra solo cuando el backend devuelve el análisis) */}
        {result && (
          <div className="p-8 bg-white rounded-xl shadow-sm border border-gray-100 mt-8 animate-fade-in">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">Resultados del Análisis</h2>
            
            <div className="flex items-center justify-center mb-8">
              <div className="relative w-32 h-32 flex items-center justify-center bg-blue-50 rounded-full border-4 border-blue-500 shadow-inner">
                <span className="text-4xl font-extrabold text-blue-700">
                  {result.match_percentage}%
                </span>
              </div>
            </div>

            <div className="mb-8">
              <h3 className="text-lg font-semibold text-gray-800 mb-3">Habilidades a Mejorar (Gap)</h3>
              <div className="flex flex-wrap gap-2">
                {result.missing_skills.map((skill: string, index: number) => (
                  <span key={index} className="px-3 py-1 bg-red-50 border border-red-200 text-red-700 rounded-full text-sm font-medium">
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <button 
              onClick={handleRestart}
              className="w-full py-3 px-4 bg-gray-100 hover:bg-gray-200 text-gray-800 font-semibold rounded-lg shadow-sm transition-colors"
            >
              Evaluar un nuevo currículum
            </button>
          </div>
        )}
        
      </main>
    </div>
  );
}

export default App;