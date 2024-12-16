import React, { useState } from "react";
import { uploadFileForPrediction } from "./api";

function Dashboard({ token }) {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file to upload.");
      return;
    }
    setError("");
    try {
      const data = await uploadFileForPrediction(token, file);
      setPrediction(data.predictedLabel || "No prediction received.");
    } catch (err) {
      setError("Error uploading file. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Dashboard</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload & Predict</button>
      {prediction && <p><strong>Prediction:</strong> {prediction}</p>}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default Dashboard;
