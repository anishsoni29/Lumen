import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time

# Function to record audio and save it as a WAV file
def record_audio(filename, duration=3, rate=16000):
    print("Recording...")
    audio_data = sd.rec(int(duration * rate), samplerate=rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording done.")
    write(filename, rate, audio_data)  # Save as WAV file

# Function to listen and process audio input
def listen_for_wake_word(rate=16000):
    print("Listening for the wake word...")
    duration = 1  # Listen in short intervals (1 second)
    volume_threshold = 2000  # Set your wake word volume threshold

    while True:
        audio_data = sd.rec(int(duration * rate), samplerate=rate, channels=1, dtype='int16')
        sd.wait()

        # Example crude approach to detect wake word using volume (this is NOT accurate)
        if np.max(audio_data) > volume_threshold:
            print("Wake word detected!")
            return True

# Main function to either record a template or detect wake word
if __name__ == "__main__":
    print("1. Record wake word template\n2. Detect wake word")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        record_audio("wake_word_template.wav")
    elif choice == "2":
        listen_for_wake_word()
    else:
        print("Invalid choice")
