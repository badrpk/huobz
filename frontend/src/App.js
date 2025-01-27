<<<<<<< HEAD
import React, { useState, useEffect } from "react";

function App() {
    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        fetch("https://your-backend-url/ai/recommend?user_id=1")
            .then((response) => response.json())
            .then((data) => setRecommendations(data.items));
    }, []);

    return (
        <div>
            <h1>Huobz Dashboard</h1>
            <h2>Recommendations</h2>
            <ul>
                {recommendations.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
=======
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
>>>>>>> ee15733af9196aa7634086c3602b7dbd4b830c07
}

export default App;
