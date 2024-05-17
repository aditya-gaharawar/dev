import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);
  const [type, setType] = useState('text');

  useEffect(() => {
    axios.get(`http://localhost:8000/data/${type}`)
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, [type]);

  return (
    <div className="App">
      <h1>Social Media Data</h1>
      <select onChange={(e) => setType(e.target.value)}>
        <option value="text">Text</option>
        <option value="image">Image</option>
        <option value="video">Video</option>
      </select>
      <ul>
        {data.map(item => (
          <li key={item._id}>{JSON.stringify(item.data)}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
