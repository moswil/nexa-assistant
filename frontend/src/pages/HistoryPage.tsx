import React, { useEffect, useState } from "react";
import { getHistory } from "../services/api";
import type { HistoryEntry } from "../types";

const HistoryPage: React.FC = () => {
    const [history, setHistory] = useState<HistoryEntry[]>([]);

    useEffect(() => {
        getHistory().then((data) => setHistory(data.history));
    }, []);

    return (
        <div>
            <h2>Conversation History</h2>
            {history.length === 0 ? (
                <p>No history yet.</p>
            ) : (
                <ul>
                    {history.map((entry, index) => (
                        <li key={index} style={{ marginBottom: "1rem" }}>
                            <strong>Q:</strong> {entry.question}
                            <br />
                            <strong>A:</strong> {entry.response}
                            <br />
                            <small>{new Date(entry.timestamp).toLocaleString()}</small>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default HistoryPage;
