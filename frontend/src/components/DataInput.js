import React, { useState } from 'react';
import axios from 'axios';

const DataInput = ({ setResults }) => {
  // State to hold form data
  const [formData, setFormData] = useState({
    start_date: '',
    end_date: '',
    bank: '',
    loan_amount: ''
  });

  // Handle input changes
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // API endpoint for the backend
    const apiUrl = 'http://127.0.0.1:5000/api/repo-market';

    try {
      // Make API request to backend
      const response = await axios.post(apiUrl, formData);

      // Set the results in the parent component
      setResults(response.data);
    } catch (error) {
      console.error('Error submitting form', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="date" name="start_date" value={formData.start_date} onChange={handleChange} required />
      <input type="date" name="end_date" value={formData.end_date} onChange={handleChange} required />
      <input type="text" name="bank" value={formData.bank} onChange={handleChange} required />
      <input type="number" name="loan_amount" value={formData.loan_amount} onChange={handleChange} required />
      <button type="submit">Submit</button>
    </form>
  );
};

export default DataInput;
