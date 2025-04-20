# Lumen

Lumen uses gemini 1.5 pro to answer questions based on what you see and hear, and it remembers those memories for you.

## Live Project Demo:
👉 [Click here to watch on YouTube](https://youtu.be/Uh7nVr40OHo)

## Working Project:
<img width="1440" alt="Screenshot 2025-04-21 at 1 10 08 AM" src="https://github.com/user-attachments/assets/fc2e8557-d505-4dd6-832a-cbcbe9648de2" />

## Hardware Requirements

- Raspberry Pi (model 4 or newer)
- Webcam
- Mini usb mic
- Logitech webcam
- Sony headphones with jack
- needed a monitor, keyboard, and mouse to interface with the pi

<img width="1440" alt="Screenshot 2025-04-20 at 4 16 53 PM" src="https://github.com/user-attachments/assets/e4792aef-5044-4c62-bdfb-e4ee564e7ab3" />

## Software Requirements

- pvporcupine
- google-generativeai
- SpeechRecognition
- firebase-admin
- google-cloud-texttospeech
- picamera2

<img width="1440" alt="Screenshot 2025-04-20 at 4 16 26 PM" src="https://github.com/user-attachments/assets/1f26b3c1-8dd2-40a4-8ecf-b299e1a5fbf4" />

## Setup

1. Clone the repository to your Raspberry Pi or local machine:
   ```
   git clone https://github.com/anishsoni29/insight-ai
   ```
2. Install the required dependencies:
   ```
   cd [repo-name]
   pip install -r requirements.txt
   ```
3. Add the neccessary api keys to the config.py file, check config.example.py

4. Make an anaconda environment to save machine space while installing the dependencies.
   ```
   conda create -n test_env
   conda activate test_env
   ```

## Usage

<img width="1440" alt="Screenshot 2025-04-20 at 4 17 11 PM" src="https://github.com/user-attachments/assets/48527869-87b9-45a6-aabc-3b710e75678a" />



### Running the Full Application (Frontend + Backend)

To run the complete application with both frontend and backend:

1. Start the frontend:
   ```
   cd speech-interface
   npm start
   ```
   This will launch the frontend at http://localhost:3000

2. In a new terminal, start the backend:
   ```
   python glasses.py
   ```

### Running Backend Only

If you only need to run the backend without the web interface:
```
python main.py
```

This will start the application in terminal mode, which will listen for the wake word and respond to speech commands.

<img width="322" alt="Screenshot 2025-04-21 at 1 08 02 AM" src="https://github.com/user-attachments/assets/97cff1a4-ed9d-400b-aea6-90ab4ca0b17f" />

## Configuration

The project's configuration can be modified by editing the `config.example.py` file and saving it as `config.py`.

## License

This project is licensed under the [License Name] - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

@anishsoni29
