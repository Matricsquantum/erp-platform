function Login() {
  return (
    <div style={{ fontFamily: 'Arial', padding: '20px', textAlign: 'center' }}>
      <h1>SynapseCore ERP Login</h1>
      <input type="text" placeholder="Username" style={{ padding: '10px', margin: '10px' }} />
      <input type="password" placeholder="Password" style={{ padding: '10px', margin: '10px' }} />
      <button style={{ padding: '10px 20px' }}>Login</button>
    </div>
  );
}
export default Login;
