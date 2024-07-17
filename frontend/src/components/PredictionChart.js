import React from 'react';

const PredictionChart = ({ data }) => {
  if (!data) return null;

  return (
    <div>
      <h2>Prediction Chart</h2>
      {/* Chart rendering logic here */}
      <p>Chart will be displayed here</p>
    </div>
  );
};

export default PredictionChart;
