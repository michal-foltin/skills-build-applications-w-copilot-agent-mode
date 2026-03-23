import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [data, setData] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace ? `https://${codespace}-8000.app.github.dev/api/leaderboard/` : null;

  useEffect(() => {
    if (!endpoint) return;
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Leaderboard API endpoint:', endpoint);
        console.log('Fetched leaderboard data:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  if (!codespace) {
    return <div className="alert alert-warning">REACT_APP_CODESPACE_NAME is not set. Leaderboard cannot be loaded.</div>;
  }

  return (
    <div className="card shadow mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-light">
              <tr>
                {data.length > 0 && Object.keys(data[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((item, idx) => (
                <tr key={item.id || idx}>
                  {data.length > 0 && Object.keys(data[0]).map((key) => (
                    <td key={key}>{typeof item[key] === 'object' ? JSON.stringify(item[key]) : item[key]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
