const API_URL = 'http://localhost:5000';

export const resolveDNS = async (data) => {
  const response = await fetch(`${API_URL}/resolve`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return response.json();
};

export const exportLogs = async (format) => {
  const response = await fetch(`${API_URL}/export?format=${format}`);
  return response.json();
};
