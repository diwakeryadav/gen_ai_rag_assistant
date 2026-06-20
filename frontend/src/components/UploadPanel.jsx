import { useState } from "react";
import { uploadFile } from "../services/api";

export default function UploadPanel() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setMessage("");
      setError("");
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    try {
      setLoading(true);
      setMessage("Uploading and ingesting document...");
      setError("");

      const res = await uploadFile(file);
      setMessage(`Successfully uploaded and indexed "${file.name}"! (${res.chunks} chunks generated)`);
      setFile(null);
      
      const fileInput = document.getElementById("file-upload");
      if (fileInput) fileInput.value = "";
    } catch (err) {
      console.error(err);
      const errMsg = err.response?.data?.detail || "Failed to upload file.";
      setError(errMsg);
      setMessage("");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-8 bg-[#111827] rounded-3xl border border-gray-800 p-8">
      <h2 className="text-3xl font-bold mb-4">
        Document Ingestion Panel
      </h2>
      <p className="text-gray-400 mb-6">
        Upload new PDF, Markdown, or text files to add them dynamically to the RAG vector database.
      </p>

      <form onSubmit={handleUpload} className="flex flex-col gap-4">
        <div className="border-2 border-dashed border-gray-700 hover:border-blue-500 transition rounded-2xl p-8 flex flex-col items-center justify-center bg-black/10 cursor-pointer relative">
          <input
            id="file-upload"
            type="file"
            accept=".pdf,.txt,.md"
            onChange={handleFileChange}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            disabled={loading}
          />
          <svg className="w-12 h-12 text-gray-500 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
          </svg>
          <p className="text-gray-300 font-medium text-lg text-center">
            {file ? file.name : "Select a PDF, TXT or MD file"}
          </p>
          <p className="text-xs text-gray-500 mt-1">
            Drag & drop or click to browse
          </p>
        </div>

        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-600 transition py-4 rounded-2xl font-semibold text-white text-lg disabled:bg-gray-800 disabled:text-gray-600 disabled:cursor-not-allowed"
          disabled={!file || loading}
        >
          {loading ? "Processing..." : "Ingest Document"}
        </button>
      </form>

      {message && (
        <div className="mt-6 bg-green-500/10 border border-green-500/20 text-green-400 rounded-2xl p-4 text-center font-medium">
          {message}
        </div>
      )}

      {error && (
        <div className="mt-6 bg-red-500/10 border border-red-500/20 text-red-400 rounded-2xl p-4 text-center font-medium">
          {error}
        </div>
      )}
    </div>
  );
}
