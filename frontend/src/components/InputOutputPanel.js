import React, { useState } from 'react';
import './InputOutputPanel.css';

function InputOutputPanel() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [loading, setLoading] = useState(false);
  const [metrics, setMetrics] = useState(null);

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = async () => {
    setLoading(true);
    setOutputText('');
    setMetrics(null);

    try {
      const response = await fetch('http://localhost:8000/inference', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          input_text: inputText,
          max_tokens: 50,
          temperature: 1.0,
          top_k: 50,
          top_p: 0.9
        })
      });

      if (!response.ok) {
        throw new Error('Failed to fetch inference results');
      }

      const data = await response.json();
      setOutputText(data.generated_text);
      setMetrics({ tokensGenerated: data.tokens_generated });
    } catch (error) {
      console.error(error);
      setOutputText('Error: Unable to generate text. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="input-output-panel">
      <textarea
        className="input-text"
        placeholder="Enter your text here..."
        value={inputText}
        onChange={handleInputChange}
      />
      <button className="submit-button" onClick={handleSubmit} disabled={loading}>
        {loading ? 'Generating...' : 'Generate'}
      </button>
      {outputText && (
        <div className="output-section">
          <h3>Generated Text:</h3>
          <p>{outputText}</p>
        </div>
      )}
      {metrics && (
        <div className="metrics-section">
          <h4>Performance Metrics:</h4>
          <p>Tokens Generated: {metrics.tokensGenerated}</p>
        </div>
      )}
    </div>
  );
}

export default InputOutputPanel;