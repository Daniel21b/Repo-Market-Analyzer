import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataInput = ({ setResults }) => {
  const [formData, setFormData] = useState({
    start_date: '',
    end_date: '',
    bank: '',
    loan_amount: ''
  });

  useEffect(() => {
    console.log('DataInput component mounted');
  }, []);

  const handleChange = (e) => {
    console.log(`Input changed: ${e.target.name} = ${e.target.value}`);
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Submit button clicked');

    try {
      console.log('Form data:', formData);
      const apiUrl = 'http://127.0.0.1:5000/api/repo-market';
      console.log('Sending request to:', apiUrl);
      
      const response = await axios.post(apiUrl, formData);
      console.log('Received response:', response.data);
      setResults(response.data);
    } catch (error) {
      console.error('Error in handleSubmit:', error);
      if (error.response) {
        console.error('Response data:', error.response.data);
        console.error('Response status:', error.response.status);
      } else if (error.request) {
        console.error('No response received:', error.request);
      } else {
        console.error('Error setting up request:', error.message);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="date" name="start_date" value={formData.start_date} onChange={handleChange} required />
      <input type="date" name="end_date" value={formData.end_date} onChange={handleChange} required />
      <input type="text" name="bank" value={formData.bank} onChange={handleChange} required />
      <input type="number" name="loan_amount" value={formData.loan_amount} onChange={handleChange} required />
      <button type="submit" onClick={() => console.log('Submit button clicked directly')}>Submit</button>
    </form>
  );
};

export default DataInput;