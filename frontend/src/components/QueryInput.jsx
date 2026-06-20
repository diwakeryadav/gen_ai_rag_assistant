import { useState } from "react";
import { queryRAG } from "../services/api";

export default function QueryInput() {

  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question) return;

    try {
      setLoading(true);
      setResponse("Thinking...");
      setSources([]);
      const data = await queryRAG(question);
      setResponse(data.answer);
      setSources(data.sources || []);
    } catch (error) {
      console.error(error);
      setResponse("Error connecting to AI backend.");
      setSources([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-8 bg-[#111827] rounded-3xl border border-gray-800 p-8">
      <h2 className="text-3xl font-bold mb-6">
        AI Query Interface
      </h2>

      <div className="flex gap-4">
        <input
          type="text"
          placeholder="Ask a question about the uploaded documents..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => { if(e.key === 'Enter') handleAsk(); }}
          className="flex-1 bg-black/30 border border-gray-700 rounded-2xl px-6 py-4 text-lg outline-none focus:border-blue-500 text-white"
          disabled={loading}
        />

        <button
          onClick={handleAsk}
          className="bg-blue-500 hover:bg-blue-600 transition px-8 rounded-2xl font-semibold text-white disabled:bg-blue-800"
          disabled={loading}
        >
          {loading ? "Asking..." : "Ask AI"}
        </button>
      </div>

      {response && (
        <div className="mt-8 bg-black/20 border border-gray-800 rounded-2xl p-6">
          <h3 className="text-xl font-semibold mb-4 text-blue-400">
            AI Response
          </h3>

          <p className="text-gray-300 leading-relaxed text-lg whitespace-pre-wrap">
            {response}
          </p>

          {sources.length > 0 && !loading && (
            <div className="mt-6 border-t border-gray-800 pt-4">
              <span className="text-xs font-bold text-gray-500 uppercase tracking-widest block mb-2">
                Sources consulted:
              </span>
              <div className="flex flex-wrap gap-2">
                {sources.map((src, index) => (
                  <span 
                    key={index}
                    className="bg-blue-500/10 text-blue-400 border border-blue-500/20 px-3 py-1 rounded-full text-xs font-semibold"
                  >
                    {src}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}