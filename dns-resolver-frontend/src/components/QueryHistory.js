import React, { useState, useEffect } from 'react';

const QueryHistory = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    // Fetch history from localStorage when the component mounts
    const savedHistory = JSON.parse(localStorage.getItem('queryHistory')) || [];
    setHistory(savedHistory);
  }, []);

  return (
    <div>
      <h2>Query History</h2>
      {history.length === 0 ? (
        <p>No queries found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Domain</th>
              <th>Query Type</th>
              <th>Result</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {history.map((entry, index) => (
              <tr key={index}>
                <td>{entry.domain}</td>
                <td>{entry.queryType}</td>
                <td>{entry.result}</td>
                <td>{entry.timestamp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default QueryHistory;
