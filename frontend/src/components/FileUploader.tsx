import { useState, DragEvent, ChangeEvent } from 'react';
import { uploadCV } from '../services/api';

// 1. Definimos la interfaz para recibir la función del componente padre
interface FileUploaderProps {
  onUploadSuccess: (sessionId: string) => void;
}

export default function FileUploader({ onUploadSuccess }: FileUploaderProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [status, setStatus] = useState<'idle' | 'uploading' | 'error'>('idle');

  const handleDragOver = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = async (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      await processFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileInput = async (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      await processFile(e.target.files[0]);
    }
  };

  const processFile = async (file: File) => {
    if (file.type !== 'application/pdf') {
      alert('Solo se aceptan archivos PDF');
      return;
    }

    setStatus('uploading');
    try {
      const data = await uploadCV(file);
      // 2. Comunicamos el éxito al componente padre (App)
      onUploadSuccess(data.session_id);
    } catch (error) {
      console.error(error);
      setStatus('error');
    }
  };

  return (
    <div className="w-full max-w-xl mx-auto p-6">
      <div
        className={`relative border-2 border-dashed rounded-xl p-12 text-center transition-all duration-200 ease-in-out
          ${isDragging ? 'border-blue-500 bg-blue-50' : 'border-gray-300 bg-white hover:border-gray-400'}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          accept=".pdf"
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          onChange={handleFileInput}
        />
        
        <div className="space-y-4 pointer-events-none">
          <div className="text-4xl">📄</div>
          <h3 className="text-lg font-semibold text-gray-700">
            Paso 1: Sube tu CV
          </h3>
          <p className="text-sm text-gray-500">Formato soportado: PDF (Máx. 5MB)</p>
        </div>
      </div>

      {status === 'uploading' && (
        <p className="mt-4 text-center text-blue-600 font-medium animate-pulse">Subiendo documento...</p>
      )}
      {status === 'error' && (
        <p className="mt-4 text-center text-red-600 font-medium">Hubo un error al subir el archivo.</p>
      )}
    </div>
  );
}