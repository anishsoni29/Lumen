import React, { useState } from 'react';
import './styles/App.css';

function App() {
  const [description, setDescription] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [userInput, setUserInput] = useState("");

  const handleCaptureAndDescribe = async (transcript) => {
    const response = await fetch("http://localhost:5001/generate-description", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_input: transcript }),
    });

    if (response.ok) {
      const data = await response.json();
      setDescription(data.description);
      
      // Trigger speech output for the description
      const speakResponse = await fetch("http://localhost:5001/speak", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: data.description }),
      });

      if (!speakResponse.ok) {
        console.error('Error speaking the description:', speakResponse.statusText);
      }
    } else {
      console.error('Error generating description:', response.statusText);
    }
  };

  const toggleVoiceRecognition = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.onstart = () => {
      setIsRecording(true);
      console.log('Voice recognition started. Try speaking into the microphone.');
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setUserInput(transcript); // Update the text area with the spoken input
      handleCaptureAndDescribe(transcript); // Immediately analyze the input
    };

    recognition.onerror = (event) => {
      console.error('Error occurred in recognition: ' + event.error);
      setIsRecording(false);
    };

    recognition.onend = () => {
      setIsRecording(false);
      console.log('Voice recognition ended.');
    };

    recognition.start(); // Start recording
  };

  return (
    <div className="app-container">
      <header>
        <h1 className="app-title">Vision for All</h1>
      </header>
      <main>
        <div className="input-card">
          <button onClick={toggleVoiceRecognition} className="record-btn">
            {isRecording ? '⏹ Stop Recording' : '🎤 Start Recording'}
          </button>
          <textarea
            className="input-area"
            value={userInput}
            readOnly
            placeholder="Your speech will appear here..."
            rows={4}
          />
        </div>
        <section className="description-section">
          <h2>{description ? `Description: ${description}` : "No description yet."}</h2>
        </section>
      </main>
      <footer>
        <p>Designed with Accessibility in Mind</p>
      </footer>
    </div>
  );
}

export default App;
