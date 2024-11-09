import React, { useState } from 'react';

const Dashboard = () => {
  const [instaUrl, setInstaUrl] = useState('');

  const handleInputChange = (e) => {
    setInstaUrl(e.target.value);
  };

  const handleButtonClick = async () => {
    if (instaUrl) {
      window.open(instaUrl, '_blank');
      try {
        const response = await fetch('http://localhost:3001/insta', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ url: instaUrl }),
        });
  
        if (response.ok) {
          console.log('URL sent successfully');
        } else {
          console.error('Error sending URL');
        }
      } catch (error) {
        console.error('Network error:', error);
      }
    }
  };
  

  return (
    <div className="d-flex flex-column justify-content-center align-items-center vh-100 bg-dark text-white">
      <h1 style={{ marginBottom: '20px' }}>Listify Social</h1>
      <div className="border rounded p-4" style={{ width: '300px', textAlign: 'center' }}>
        <div className="input-group">
          <input
            type="text"
            className="form-control"
            placeholder="Connect your social handle"
            value={instaUrl}
            onChange={handleInputChange}
          />
          <button className="btn btn-outline-secondary" onClick={handleButtonClick}>
            Go
          </button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
