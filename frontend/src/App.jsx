import QueryInput from "./components/QueryInput";
import UploadPanel from "./components/UploadPanel";

export default function App() {

  return (
    <div className="min-h-screen bg-[#0B0F14] text-white p-6 md:p-10">
      <div className="max-w-7xl mx-auto space-y-8">
        
        <div className="bg-[#111827] rounded-3xl border border-gray-800 p-8 md:p-10">
          <h1 className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-400 to-indigo-500 bg-clip-text text-transparent">
            Intelligence RAG Platform
          </h1>
          <p className="text-gray-400 mt-4 text-base md:text-lg max-w-2xl">
            A secure, localized Retrieval-Augmented Generation assistant. Upload documents dynamically and ask context-grounded questions.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-5 gap-8">
          <div className="lg:col-span-2">
            <UploadPanel />
          </div>
          
          <div className="lg:col-span-3">
            <QueryInput />
          </div>
        </div>

      </div>
    </div>
  );
}