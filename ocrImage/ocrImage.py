from flask import Flask, request, jsonify
from PIL import Image
import pytesseract as tess

# Set Tesseract executable and TESSDATA_PREFIX
tess.pytesseract.tesseract_cmd = r'C:\Users\borha\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Users\borha\AppData\Local\Programs\Tesseract-OCR\tessdata'

app = Flask(__name__)

@app.route('/initialize', methods=['POST'])
def initialize():
    return jsonify({'message': 'Arabic OCR API initialized successfully.'})

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    # Check if an image file is uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image_file = request.files['image']

    # Load the image
    image = Image.open(image_file)

    # Perform OCR
    arabic_text = tess.image_to_string(image, lang='ara')

    return jsonify({'text': arabic_text})

if __name__ == '__main__':
    app.run(debug=True)
