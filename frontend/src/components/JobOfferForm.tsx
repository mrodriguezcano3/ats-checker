import { useState } from 'react';
import { analyzeMatch } from '../services/api';

interface JobOfferFormProps {
  sessionId: string;
  onAnalysisComplete: (result: any) => void;
}

export default function JobOfferForm({ sessionId, onAnalysisComplete }: JobOfferFormProps) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !description.trim()) return;

    setIsAnalyzing(true);
    try {
      const result = await analyzeMatch(sessionId, title, description);
      onAnalysisComplete(result);
    } catch (error) {
      console.error(error);
      alert('Error en el análisis');
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto mt-8 p-6 bg-white rounded-xl shadow-sm border border-gray-100">
      <h3 className="text-xl font-bold text-gray-800 mb-4">Paso 2: Detalles de la Oferta</h3>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Puesto de trabajo</label>
          <input
            type="text"
            className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
            placeholder="Ej. Software Engineer Junior"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            disabled={isAnalyzing}
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Descripción de la oferta</label>
          <textarea
            className="w-full p-2 border border-gray-300 rounded-lg h-32 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none resize-none"
            placeholder="Pega aquí los requisitos y la descripción del puesto..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            disabled={isAnalyzing}
          />
        </div>
        <button
          type="submit"
          disabled={isAnalyzing || !title || !description}
          className="w-full py-3 px-4 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-md transition-colors disabled:bg-gray-400"
        >
          {isAnalyzing ? 'Procesando con IA...' : 'Analizar Compatibilidad'}
        </button>
      </form>
    </div>
  );
}