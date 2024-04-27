from flask import Flask, request, jsonify 
from flask_cors import CORS
import os
import google.generativeai as genai
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Configure generative AI with the API key
genai.configure(api_key=api_key)

# Initialize the generative model
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)
CORS(app)

# Define the instruction template
instruction = """
Chatbot, assume the role of a virtual executive assistant and prepare your self to answer only from the forthcoming data.
"""

# Initialize the chat with empty history
chat = None

@app.route('/initialize', methods=['POST'])
def initialize():
    global chat

    # Get the initial data from the request
    initial_data = request.json.get('initial_data')

    # Initialize the chat with the initial data
    chat = model.start_chat(history=[])
    chat.send_message( instruction + initial_data)
    return jsonify({'message': 'Chatbot initialized successfully.'})

@app.route('/ask', methods=['POST'])
def ask():
    global chat

    if chat is None:
        return jsonify({'error': 'Chatbot has not been initialized. Please initialize first.'})

    # Get the question from the request data
    question = request.json.get('question')

    # Send the question to the chatbot
    response = chat.send_message(question)

    # Return the bot's response
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5005)
