import axios from "axios";
import type { AskRequest, AskResponse, HistoryResponse } from "../types";

const api = axios.create({
    baseURL: "http://localhost:8000/api/v1",
});

export const askQuestion = async (payload: AskRequest) => {
    const response = await api.post<AskResponse>("/ask", payload);
    return response.data;
};

export const getHistory = async () => {
    const response = await api.get<HistoryResponse>("/history");
    return response.data;
};
