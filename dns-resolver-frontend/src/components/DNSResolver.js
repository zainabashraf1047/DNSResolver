import React, { useState } from 'react';
import './DNSResolver.css'; // Import custom CSS file
import ExportLogs from './ExportLogs'; // Import ExportLogs component
import QueryHistory from './QueryHistory'; // Import QueryHistory component
import { resolveDNS } from '../api';

const DNSResolver = () => {
  const [domain, setDomain] = useState('');
  const [queryType, setQueryType] = useState('A');
  const [method, setMethod] = useState('recursive');
  const [results, setResults] = useState('');
  const [historyVisible, setHistoryVisible] = useState(false);

  const handleResolve = async () => {
    const response = await resolveDNS({ domain, query_type: queryType, method });
    setResults(response.results ? response.results.join(', ') : response.error);
  };

  const toggleHistory = () => {
    setHistoryVisible(!historyVisible);
  };

  return (
    <div className="dns-container">
      <div className="input-container">
        <h2>DNS Resolver</h2>
        <div className="input-field">
          <input
            type="text"
            placeholder="Enter domain"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
          />
        </div>
        <div className="select-field">
          <select value={queryType} onChange={(e) => setQueryType(e.target.value)}>
            <option value="A">A</option>
            <option value="AAAA">AAAA</option>
            <option value="MX">MX</option>
            <option value="CNAME">CNAME</option>
            <option value="PTR">PTR</option>
          </select>
        </div>
        <div className="select-field">
          <select value={method} onChange={(e) => setMethod(e.target.value)}>
            <option value="recursive">Recursive</option>
            <option value="iterative">Iterative</option>
          </select>
        </div>
        <div className="button-container">
          <button onClick={handleResolve}>Resolve</button>
        </div>
      </div>

      {/* Only render ExportLogs once */}
     {  <ExportLogs />}

      {/* Results Container */}
      <div className="results-history-container">
        <div className="result-container">
          <h3>Results</h3>
          <p>{results}</p>
        </div>

        {/* Only show QueryHistory when historyVisible is true */}
        <div className="history-container">
          <button className="toggle-history" onClick={toggleHistory}>
            {historyVisible ? 'Hide Queries' : 'Show Queries'}
          </button>
          {historyVisible && <QueryHistory />}
        </div>
      </div>
    </div>
  );
};

export default DNSResolver;
