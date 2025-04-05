function Dashboard() {
  return (
    <div style={{ fontFamily: 'Arial', padding: '20px', maxWidth: '100%', boxSizing: 'border-box' }}>
      <h1>SynapseCore ERP Dashboard</h1>
      <nav style={{ background: '#f0f0f0', padding: '15px', marginBottom: '20px' }}>
        <a href="#home" style={{ marginRight: '15px' }}>Home</a> | 
        <a href="#accounting">Accounting</a> | 
        <a href="#ai">AI Insights</a>
      </nav>
      <div style={{ border: '2px solid #333', padding: '20px', marginTop: '20px' }}>
        <h2>Quick Stats</h2>
        <p>Revenue: $1,000 | Expenses: $500</p>
        <p>AI Data Placeholder</p>
      </div>
    </div>
  );
}
export default Dashboard;