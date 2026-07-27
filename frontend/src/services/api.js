import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const queryRAG = async (question) => {
  const response = await API.post("/query", {
    question,
  });
  return response.data;
};

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await API.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return response.data;
};