
import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSend = async () => {
    const res = await fetch('http://localhost:8000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Tally Assistant – Demo</h1>
      <input value={question} onChange={e => setQuestion(e.target.value)} placeholder="Ask something..." />
      <button onClick={handleSend}>Send</button>
      <p><strong>Response:</strong> {response}</p>
    </div>
  );
}

export default App;
