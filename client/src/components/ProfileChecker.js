import React, { useState } from 'react';
import axios from 'axios';

const ProfileChecker = () => {
  const [profileURL, setProfileURL] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Call the Flask backend endpoint
      const response = await axios.post('http://localhost:5000/api/analyze', { profile_url: profileURL });
      setResult(response.data);
    } catch (error) {
      console.error('Error analyzing profile:', error);
      setResult({ error: 'Failed to analyze profile.' });
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Profile URL:
          <input
            type="text"
            value={profileURL}
            onChange={(e) => setProfileURL(e.target.value)}
            style={{ marginLeft: '10px', width: '300px' }}
            placeholder="Enter profile link"
          />
        </label>
        <button type="submit" style={{ marginLeft: '10px' }}>Analyze</button>
      </form>
      {result && (
        <div style={{ marginTop: '20px' }}>
          <h4>Analysis Result:</h4>
          {result.error ? (
            <p style={{ color: 'red' }}>{result.error}</p>
          ) : (
            <div>
              <p><strong>Profile:</strong> {result.profile_url}</p>
              <p><strong>Prediction:</strong> {result.prediction}</p>
              <p><strong>Confidence:</strong> {result.confidence}%</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ProfileChecker;
