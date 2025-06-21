import React, { useState } from "react";
import { askQuestion } from "../services/api";

const AskPage: React.FC = () => {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const handleAsk = async () => {
        if (!question.trim()) return;
        const response = await askQuestion({ question });
        setAnswer(response.response);
        setQuestion("");
    };

    return (
        <div>
            <h2>Ask the Assistant</h2>
            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Type your question"
                style={{ width: "100%", padding: "0.5rem" }}
            />
            <button onClick={handleAsk} disabled={!question.trim()}>
                Send
            </button>
            {answer && (
                <div style={{ marginTop: "1rem" }}>
                    <strong>Answer:</strong>
                    <p>{answer}</p>
                </div>
            )}
        </div>
    );
};

export default AskPage;
