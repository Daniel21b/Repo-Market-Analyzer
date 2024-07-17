import React, { useState } from 'react';
import Header from './components/Header';
import DataInput from './components/DataInput';
import AnalysisResults from './components/AnalysisResults';
import PredictionChart from './components/PredictionChart';
import Footer from './components/Footer';
import './App.css';

const App = () => {
  const [results, setResults] = useState(null);

  return (
    <div className="app-container">
      <Header />
      <main className="main-content">
        <section className="data-input-section">
          <h2 className="section-title">Data Input</h2>
          <DataInput setResults={setResults} />
        </section>
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