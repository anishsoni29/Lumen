# Lumen

Lumen uses gemini 1.5 pro to answer questions based on what you see and hear, and it remembers those memories for you.

## Working Project:
![773193c5-d78e-4345-9599-a421b44d9a8a](https://github.com/user-attachments/assets/76a4d031-2663-4d36-bbcb-0c0a0998704c)

## Hardware Requirements

- Raspberry Pi (model 4 or newer)
- Webcam
- Mini usb mic
- Logitech webcam
- Sony headphones with jack
- needed a monitor, keyboard, and mouse to interface with the pi

## Software Requirements

- pvporcupine
- google-generativeai
- SpeechRecognition
- firebase-admin
- google-cloud-texttospeech
- picamera2

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
![34fc0f66-a7ca-45cb-9b5d-dd9f514cdf56](https://github.com/user-attachments/assets/bb75d58e-38d0-4e87-a3e0-96d48969efb5)

1. Run the main script:
   ```
   python main.py
   ```

## Configuration

The project's configuration can be modified by editing the `config.example.py` file and saving it as `config.py`.

## License

This project is licensed under the [License Name] - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

@anishsoni29
