import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./Login";
import Dashboard from "./Dashboard";
import "./styles.css";

function App() {
  const [token, setToken] = useState(null);

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={!token ? <Login setToken={setToken} /> : <Navigate to="/dashboard" />}
        />
        <Route
          path="/dashboard"
          element={token ? <Dashboard token={token} /> : <Navigate to="/" />}
        />
      </Routes>
    </Router>
  );
}

export default App;
