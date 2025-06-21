import { useState } from 'react';

type AskResponse = {
  response: string;
};

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/api/v1/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      const data: AskResponse = await res.json();
      setResponse(data.response);
    } catch (err) {
      console.error('Failed to ask:', err);
      setResponse('Something went wrong.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', padding: '1rem' }}>
      <h2>Ask the Assistant</h2>
      <textarea
        rows={3}
        style={{ width: '100%' }}
        placeholder="Type your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <br />
      <button onClick={handleAsk} disabled={loading}>
        {loading ? 'Sending...' : 'Send'}
      </button>

      {response && (
        <div style={{ marginTop: '1rem', background: '#f4f4f4', padding: '1rem' }}>
          <strong>Answer:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
