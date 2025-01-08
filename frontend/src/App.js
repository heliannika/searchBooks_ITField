import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

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

    // Onko kuvaus näkyvissä
    const [visibleDescriptionId, setVisibleDescriptionId] = useState(null);

    // Togglataan tila näkyviin/näkymättömäksi
    const toggleDescription = (id) => {
      setVisibleDescriptionId(visibleDescriptionId === id ? null : id);
    };
  

    return (
        <div className="app-container">
            <h1 className="heading">Hae kirjaa</h1>
            <div className="search-bar">
              <input
                  type="text"
                  className="search-input"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Hae kirjan/alagenren/kirjailijan mukaan..."
              />
              <button className="search-button" onClick={handleSearch}>Etsi</button>
            </div>

            <ul className="results-list">
                {/* Listaus hakutuloksista */}
                {results.map((item) => (
                    <li key={item.id} className="result-item">
                      <div>
                        <strong className="result-b" onClick={() => toggleDescription(item.id)}>{item.book}, author: {item.author}</strong>
                      </div>
                      {visibleDescriptionId === item.id && (
                        <div>
                          {item.description}
                        </div>
                      )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;