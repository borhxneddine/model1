from flask import Flask, request, jsonify
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/get_pdf_text', methods=['POST'])
def get_pdf_text():
    if 'pdfs' not in request.files:
        return jsonify({'error': 'No PDFs uploaded'}), 400

    pdfs = request.files.getlist('pdfs')
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return jsonify({'text': text}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
