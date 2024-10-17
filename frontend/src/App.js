import React, { useState } from 'react';

function App() {
  const [description, setDescription] = useState("");
  const [voiceInput, setVoiceInput] = useState("");

  // Function to capture voice using Web Speech API
  const handleVoiceInput = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setVoiceInput(transcript);
    };
    recognition.start();
  };

  // Function to send voice input to backend and get response
  const handleSubmit = async () => {
    const response = await fetch("http://localhost:5001/generate-description", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_input: voiceInput }),
    });

    const data = await response.json();
    setDescription(data.description);

    // Optionally trigger speech output
    await fetch("http://localhost:5001/speak", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: data.description }),
    });
  };

  return (
    <div className="App">
      <h1>Image Caption Generator</h1>
      <button onClick={handleVoiceInput}>Start Voice Input</button>
      <p>{voiceInput ? `You said: ${voiceInput}` : "Waiting for input..."}</p>
      <button onClick={handleSubmit}>Generate Caption</button>
      <h2>{description ? `Description: ${description}` : "No description yet."}</h2>
    </div>
  );
}

export default App;
