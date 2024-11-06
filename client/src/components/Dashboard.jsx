import React, { useState } from 'react';

const Dashboard = () => {
  const [instaUrl, setInstaUrl] = useState('');

  const handleInputChange = (e) => {
    setInstaUrl(e.target.value);
  };

  const handleButtonClick = () => {
    if (instaUrl) {
      window.open(instaUrl, '_blank');
    }
  };

  return (
    <div className="d-flex flex-column justify-content-center align-items-center vh-100 bg-dark text-white">
      <h1 style={{ marginBottom: '20px' }}>AyushFitness</h1>
      <div className="border rounded p-4" style={{ width: '300px', textAlign: 'center' }}>
        <div className="input-group">
          <input
            type="text"
            className="form-control"
            placeholder="Connect to Insta"
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
