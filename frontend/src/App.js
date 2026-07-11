import React from 'react';
import './App.css';
import InputOutputPanel from './components/InputOutputPanel';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Speculative Speculative Decoding</h1>
        <p>Welcome to the SSD frontend!</p>
      </header>
      <main>
        <InputOutputPanel />
      </main>
    </div>
  );
}

export default App;