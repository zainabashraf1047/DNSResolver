import React from 'react';

const ExportLogs = () => {
  const handleExport = async (format) => {
    try {
      const response = await fetch(`/export/${format}`);
      if (!response.ok) {
        const data = await response.json();
        alert(data.message || 'Failed to export logs.');
        return;
      }
      // Create a downloadable file
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `dns_queries.${format}`;
      link.click();
      alert('Logs exported successfully!');
    } catch (error) {
      alert('There was an error exporting the logs.');
    }
  };

  return (
    <div>
      <h2>Export Logs</h2>
      <button onClick={() => handleExport('json')}>Export to JSON</button>
      <button onClick={() => handleExport('csv')}>Export to CSV</button>
    </div>
  );
};

export default ExportLogs;
