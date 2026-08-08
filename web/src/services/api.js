const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function chat(message) {
  const response = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  return response.json();
}
