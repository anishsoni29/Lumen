import os
from gtts import gTTS
from pydub import AudioSegment
import simpleaudio as sa

def generate_audio(text, lang='en'):
    """Generate an audio file from the given text."""
    tts = gTTS(text=text, lang=lang)
    temp_audio_file = 'temp_output.mp3'
    tts.save(temp_audio_file)
    return temp_audio_file

def convert_mp3_to_wav(mp3_file):
    """Convert MP3 file to WAV format."""
    wav_file = mp3_file.replace('.mp3', '.wav')
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')
    return wav_file

def play_audio(file_path):
    """Play the generated audio file."""
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def speak(text):
    """Convert text to speech, save as audio, convert to WAV, and play it."""
    temp_file_path = generate_audio(text)
    
    print(f"Audio content generated for text: '{text}'")
    
    # Convert MP3 to WAV
    wav_file_path = convert_mp3_to_wav(temp_file_path)
    
    play_audio(wav_file_path)

    # Optionally remove the temporary files after playing
    os.remove(temp_file_path)
    os.remove(wav_file_path)

if __name__ == "__main__":
    speak("This is a test to check the audio output.")
