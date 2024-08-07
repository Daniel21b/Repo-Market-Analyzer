import React, { useState } from 'react';
import axios from 'axios';
import DataInput from './components/DataInput';
import AnalysisResults from './components/AnalysisResults';
import PredictionChart from './components/PredictionChart';
import Footer from './components/Footer';
import fedImage from './images/Fed.jpg';
import './App.css';

const Header = () => (
  <header className="app-header">
    <div className="header-content">
      <div className="logo">Repo Market Analyzer</div>
      <nav>
        <ul>
          <li><a href="#features">Features</a></li>
          <li><a href="#analysis">Analysis</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>
);

const App = () => {
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (formData) => {
    try {
      console.log("Form data: ", formData);
      console.log("Sending request to: http://127.0.0.1:5000/api/repo-market");

      const response = await axios.post('http://127.0.0.1:5000/api/repo-market', formData, {
        headers: {
          'Content-Type': 'application/json',
        }
      });

      console.log("Response received: ", response.data);
      setResults(response.data);
      setError(null);
    } catch (error) {
      console.error("Error in handleSubmit: ", error);
      setError("An error occurred while processing your request. Please try again.");
    }
  };

  return (
    <div className="app-container">
      <Header />
      <main className="main-content">
        <section className="hero-section">
          <div className="hero-content">
            <h1>Repo Market Analyzer</h1>
            <h2>Small Steps To A Better Future</h2>
            <p>Analyze repo market trends and make informed decisions with real-time data and advanced analytics.</p>
            <div className="cta-buttons">
              <button className="cta-primary">Get Started</button>
              <button className="cta-secondary">
                <span className="play-icon">▶</span> Watch Video
              </button>
            </div>
          </div>
          <div className="hero-image">
            <img src={fedImage} alt="Federal Reserve Building" />
          </div>
        </section>

        <section id="features" className="features-section">
          <div className="feature-card">
            <h3>Real-time repo rate tracking</h3>
          </div>
          <div className="feature-card">
            <h3>Cross-collateral analysis</h3>
          </div>
          <div className="feature-card">
            <h3>Regulatory compliance tools</h3>
          </div>
        </section>

        <section id="analysis" className="data-input-section">
          <h2 className="section-title">Data Input</h2>
          <DataInput onSubmit={handleSubmit} />
        </section>

        {error && <div style={{ color: 'red' }}>{error}</div>}

        {results && (
          <>
            <section className="analysis-results-section">
              <h2 className="section-title">Analysis Results</h2>
              <AnalysisResults results={results} />
            </section>
            <section className="prediction-chart-section">
              <h2 className="section-title">Prediction Chart</h2>
              <PredictionChart data={results} />
            </section>
          </>
        )}
      </main>
      <Footer />
    </div>
  );
};

export default App;
