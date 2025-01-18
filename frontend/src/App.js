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
}

export default App;
