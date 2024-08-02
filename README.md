# Repo Market Analyzer

## Overview

The Repo Market Analyzer is a web application that allows users to analyze and predict trends in the repo (repurchase agreement) market. It provides a user-friendly interface for inputting market data and visualizes the analysis results.

## Features

- Data input form for specifying analysis parameters
- Interest rate prediction based on input data
- Market analysis visualization
- Risk assessment display

## Tech Stack

- Frontend: React.js
- Backend: Flask (Python)
- API Communication: Axios

## Project Structure

```
repo-market-analyzer/
│
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── DataInput.js
│   │   ├── AnalysisResults.js
│   │   ├── PredictionChart.js
│   │   └── Footer.js
│   │
│   ├── App.js
│   └── App.css
│
├── public/
│   └── index.html
│
└── README.md
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/repo-market-analyzer.git
   ```

2. Navigate to the project directory:
   ```
   cd repo-market-analyzer
   ```

3. Install dependencies:
   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

5. Open your browser and visit `http://localhost:3000`

## Usage

1. Fill out the data input form with the following information:
   - Start Date
   - End Date
   - Bank Name
   - Loan Amount

2. Click the "Submit" button to send the data for analysis.

3. View the analysis results, including:
   - Interest Rate Prediction
   - Market Analysis
   - Risk Assessment

4. Examine the Prediction Chart for visual representation of the data.

## API Endpoints

The frontend communicates with the backend using the following API endpoint:

- POST `/api/repo-market`: Sends market data for analysis and receives prediction results.

## Troubleshooting

If you encounter issues with the submit button not responding:

1. Check the browser console for any error messages.
2. Ensure all required fields in the form are filled out.
3. Verify that the backend server is running and accessible at `http://127.0.0.1:5000`.
4. Check for any CORS-related issues in the browser console.

## Contributing

Contributions to the Repo Market Analyzer are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
