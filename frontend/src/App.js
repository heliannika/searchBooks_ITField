import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        try {
            // Haku backendille
            const response = await axios.get(`http://127.0.0.1:5000/api/search`, {
                params: { query }
            });
            // Hakutulosten tallennus
            setResults(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Hae kirjaa</h1>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Hae kirjan mukaan..."
            />
            <button onClick={handleSearch}>Etsi</button>

            <ul>
                {/* Listaus hakutuloksista */}
                {results.map((item) => (
                    <li key={item.id}>
                        <strong>{item.book}</strong>: {item.description} (kirjailija: {item.author}, alagenren ID: {item.subgenre_id})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;