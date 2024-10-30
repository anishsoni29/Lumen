from flask import Flask, request, jsonify
import os
import tempfile
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from picture import take_picture
import threading
from gtts import gTTS
import pygame  # Updated to use pygame

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Pygame Mixer
pygame.mixer.init()

# Initialize the image captioning model from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Helper function to create image folder
def get_image_folder(folder_name="CapturedImages"):
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

# Function to generate description for the captured image
def generate_image_description(image_path):
    image = Image.open(image_path)
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    description = processor.decode(out[0], skip_special_tokens=True)
    return description

# Function to speak text using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    audio_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(audio_file.name)

    # Use pygame to play the audio
    pygame.mixer.music.load(audio_file.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for music to finish playing
        pygame.time.Clock().tick(10)

# Call this function whenever you want to speak out the text
@app.route('/speak', methods=['POST'])
def speak_endpoint():
    data = request.json
    text = data.get('text', '')  # Get the text to speak from the request
    if text:
        print(f"Speaking: {text}")  # Debug print
        threading.Thread(target=speak, args=(text,)).start()  # Speak in a separate thread
        return jsonify({"message": "Speaking started"}), 200
    return jsonify({"error": "No text provided"}), 400

# Route for handling image capture and description generation
@app.route('/generate-description', methods=['POST'])
def generate_description():
    data = request.json
    user_input = data.get("user_input")

    # Announce that a picture is being taken
    speak_thread = threading.Thread(target=speak, args=("Taking a picture, please wait.",))
    speak_thread.start()

    # Folder for saving images
    folder_name = "CapturedImages"
    image_folder = get_image_folder(folder_name)

    # Simulating the take_picture functionality
    sanitized_input = ''.join(e for e in user_input if e.isalnum() or e == ' ').replace(' ', '_')
    filepath = os.path.join(image_folder, f'{sanitized_input}.jpg')

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        filepath = temp_file.name
        take_picture(filepath)

    description = generate_image_description(filepath)

    # Announce the generated description
    speak_thread = threading.Thread(target=speak, args=(description,))
    speak_thread.start()

    # Return description as JSON response
    return jsonify({"description": description})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
