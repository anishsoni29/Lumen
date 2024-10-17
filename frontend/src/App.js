import React, { useState } from 'react';

function App() {
  const [description, setDescription] = useState("");
  const [userInput, setUserInput] = useState("");

  // Function to handle input change
  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  // Function to send request to backend for capturing an image and getting description
  const handleCaptureAndDescribe = async () => {
    const response = await fetch("http://localhost:5001/generate-description", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_input: userInput }),  // Send user input to the backend
    });

    if (response.ok) {  // Check if the response is successful
      const data = await response.json();
      setDescription(data.description);
      setUserInput("");  // Clear input after submission

      // Trigger speech output for the description
      const speakResponse = await fetch("http://localhost:5001/speak", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: data.description }),  // Send description for TTS
      });

      if (speakResponse.ok) {
        console.log('Speech request sent successfully');
      } else {
        console.error('Error speaking the description:', speakResponse.statusText);
      }
    } else {
      console.error('Error generating description:', response.statusText);
    }
};


  // Function to start voice recognition
  const startVoiceRecognition = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.onstart = () => {
      console.log('Voice recognition started. Try speaking into the microphone.');
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setUserInput(transcript);  // Set the recognized text to userInput
    };

    recognition.onerror = (event) => {
      console.error('Error occurred in recognition: ' + event.error);
    };

    recognition.onend = () => {
      console.log('Voice recognition ended.');
    };

    recognition.start();
  };

  return (
    <div className="App">
      <h1>Image Caption Generator</h1>
      <textarea 
        value={userInput} 
        onChange={handleInputChange} 
        placeholder="Type your question here..." 
        rows={4} 
        cols={50} 
      />
      <br />
      <button onClick={startVoiceRecognition} style={{ marginRight: "10px" }}>
        🎤 Start Speaking
      </button>
      <button onClick={handleCaptureAndDescribe}>Capture Image and Generate Description</button>
      <h2>{description ? `Description: ${description}` : "No description yet."}</h2>
    </div>
  );
}

export default App;
