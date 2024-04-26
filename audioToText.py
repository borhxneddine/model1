import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the recognizer
recognizer = sr.Recognizer()

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        # Get audio file from request
        audio_file = request.files['audio']
        
        # Read the audio data
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        
        # Use the recognizer to transcribe the audio
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        
        # Return transcription
        return jsonify({'transcription': text})
    except sr.UnknownValueError:
        return jsonify({'error': 'Speech recognition could not understand the audio'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Error during speech recognition: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
