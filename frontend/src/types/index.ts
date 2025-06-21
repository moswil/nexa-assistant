export interface AskResponse {
    response: string;
}

export interface AskRequest {
    question: string;
}

export interface HistoryEntry {
    question: string;
    response: string;
    timestamp: string;
}

export interface HistoryResponse {
    history: HistoryEntry[];
}
