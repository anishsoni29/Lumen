from flask import Flask, request, jsonify
import os
import tempfile
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from picture import take_picture
import pyttsx3


from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Initialize TTS engine
engine = pyttsx3.init()

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

# Route for handling image capture and description generation
@app.route('/generate-description', methods=['POST'])
def generate_description():
    data = request.json
    user_input = data.get("user_input")

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

    # Return description as JSON response
    return jsonify({"description": description})

# Route to handle text-to-speech
@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text")
    
    # Convert text to speech and respond
    engine.say(text)
    engine.runAndWait()
    
    return jsonify({"message": "Spoken successfully"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
