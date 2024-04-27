**FILE(PDF,IMAGE,AUDIO) Processor and Conversational AI Interaction Tool**

---

### Purpose
This tool combines FILE processing capabilities with conversational AI interaction to enable users to extract insights from FILE documents and interact with a generative AI model seamlessly. It serves as a versatile utility for both document analysis and conversational interactions.
### Models
1 PDF Processor: Utilizes PyPDF2 library for extracting text from PDF documents. The extracted text is then split into smaller, manageable chunks for further processing.
2 Conversational AI Model: Integrates Google's generative AI API to create a conversational retrieval chain. This model is designed to respond to user queries and engage in meaningful conversations based on the input.
3 Audio Transcription Model: Utilizes the SpeechRecognition library to transcribe audio files into text. This model supports multiple languages and provides accurate transcriptions for various audio formats.
4 Parking Ticket Summary Generator: Utilizes a conversational AI model to generate detailed parking ticket summaries based on provided data. It gathers relevant information such as date, time, location, and additional notes to create comprehensive summaries.
5 Executive Summary Generator: Employs a conversational AI model to act as a virtual executive assistant, producing detailed summaries based on incoming data. It extracts key points, action items, and meeting objectives to create concise yet informative executive summaries.
6 Image OCR: Performs optical character recognition (OCR) on images to extract text. This model is useful for digitizing text content from images, enabling further processing and analysis.
7 Image Description Model (Gemini): Integrates OCR technology with generative AI capabilities to describe the content of images. This model analyzes image content and generates descriptive summaries based on the recognized objects, scenes, or text within the images.

### Endpoints and Request Body

1. **GET /get_pdf_text**
   - **Request Body**: 
     - `pdfs`: List of PDF files to process.
   - **Response**: 
     - `text`: Extracted text from the PDF files.

2. **POST /generate_summary**
   - **Request Body**: 
     - `data`: Data to be summarized.
   - **Response**: 
     - `summary`: Detailed summary generated based on the input data.

3. **POST /generate_pv**
   - **Request Body**: 
     - `data`: Data to generate parking ticket summary.
   - **Response**: 
     - `parking_ticket_summary`: Detailed parking ticket summary.

4. **POST /initialize**
   - **Request Body**: 
     - `initial_data`: Initial data to initialize chatbot.
   - **Response**: 
     - `message`: Confirmation message indicating successful initialization.

5. **POST /ask**
   - **Request Body**: 
     - `question`: User's question.
   - **Response**: 
     - `response`: Response from the chatbot based on the provided question.

6. **POST /transcribe**
   - **Request Body**: 
     - `audio`: Audio file for transcription.
   - **Response**: 
     - `transcription`: Transcribed text from the audio file.
    
    AND MORE

### Usage
1. **Processing PDFs**:
   - Upload PDF files using the `/get_pdf_text` endpoint to extract text.
   - Process the extracted text using the conversational AI model.

2. **Interacting with Conversational AI**:
   - Initialize the chatbot with `/initialize` endpoint.
   - Ask questions or provide data for summarization using `/ask` or `/generate_summary` endpoints.
   - Receive responses or summaries from the chatbot.

3. **Transcribing Audio**:
   - Upload audio files using the `/transcribe` endpoint to transcribe speech into text.

AND MORE 

### Dependencies
- Flask: Web framework for building RESTful APIs.
- PyPDF2: Library for extracting text from PDF documents.
- Hugging Face Transformers: Library for natural language processing tasks, used for embeddings.
- Faiss: Library for efficient similarity search and clustering of dense vectors.
- Google Generative AI API: Provides access to state-of-the-art generative models for natural language processing.
  
AND MORE

### Setup
1. Install dependencies: `pip install -r requirements.txt` for each model 
2. Set up environment variables, including the Google API key.
3. Run the Flask server: `python nameOfModel.py`

### Contributions
Contributions are welcome! Feel free to submit issues or pull requests for any improvements or new features.
