import React from 'react';

const AnalysisResults = ({ results }) => {
  if (!results) return null;

  return (
    <div>
      <h2>Analysis Results</h2>
      <p>Interest Rate Prediction: {results.interest_rate_prediction}</p>
      <p>Market Analysis: {JSON.stringify(results.market_analysis)}</p>
      <p>Risk Assessment: {JSON.stringify(results.risk_assessment)}</p>
    </div>
  );
};

export default AnalysisResults;
