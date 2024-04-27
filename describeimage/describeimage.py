from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path    
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
model = genai.GenerativeModel("gemini-pro-vision")

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Resource Sharing for all routes

@app.route('/generate_description', methods=['POST'])
def generate_description():
    # Check if the 'file' key is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    # Get the file from the request
    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Check if the file is an image
    if file and file.mimetype.startswith('image'):
        # Save the image to a temporary file
        image_path = Path("temp_image.jpeg")
        file.save(image_path)
        
        # Read the image bytes
        image_bytes = image_path.read_bytes()
        
        # Generate description prompt
        prompt = ["describe the image", {"mime_type": file.mimetype, "data": image_bytes}]
        
        # Generate content using the model
        response = model.generate_content(prompt)
        
        # Return the generated description
        return jsonify({"description": response.text}), 200
    
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(debug=True)
