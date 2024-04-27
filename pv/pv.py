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

@app.route('/generate_pv', methods=['POST'])
def generate_parking_ticket_summary():
    # Get data from the request
    data = request.json.get('data')

    # Define the instruction template
    instruction = """
    Chatbot, please create a thorough and detailed parking ticket summary including all relevant information such as date, time, 
    location,include details about any upcoming meetings , including the list of attendees, tasks assigned to each attendee, 
    and the objectives of the meeting and any additional notes that need to be documented, based on the forthcoming data .
        """

    # Initialize the chat with empty history
    chat = model.start_chat(history=[])

    # Send the question along with the instruction to the chatbot
    response = chat.send_message(instruction + data)

    # Return the generated response
    return jsonify({'parking_ticket_summary': response.text})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5007)
