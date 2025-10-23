import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/api/health")
      .then((res) => res.json())
      .then((data) => setStatus(`✅ ${data.service} is Online`))
      .catch(() => setStatus("❌ API Offline"));
  }, []);

  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        display: "flex",
        height: "100vh",
        alignItems: "center",
        justifyContent: "center",
        flexDirection: "column",
        background: "#111",
        color: "#0f0",
        fontSize: "1.5rem",
      }}
    >
      <h1>TwinViz 3D Builder</h1>
      <p>{status}</p>
    </div>
  );
}

export default App;
