import getpass
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import faiss
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# extracting text from pdf
def get_pdf_text(docs):
    text = ""
    for pdf in docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# converting text to chunks
def get_chunks(raw_text):
    text_splitter = CharacterTextSplitter(separator="\n",
                                          chunk_size=1000,
                                          chunk_overlap=200,
                                          length_function=len)
    chunks = text_splitter.split_text(raw_text)
    return chunks

# using all-MiniLm embeddings model and faiss to get vectorstore
def get_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    vectorstore = faiss.FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore

# generating conversation chain
def get_conversationchain(vectorstore):
    if vectorstore is None:
        raise ValueError("Vectorstore cannot be None.")
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    memory = ConversationBufferMemory(memory_key='chat_history',
                                      return_messages=True,
                                      output_key='answer')  # using conversation buffer memory to hold past information
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory)
    return conversation_chain

def process_pdf(docs, conversation):
    raw_text = get_pdf_text(docs)
    text_chunks = get_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    conversation['vectorstore'] = vectorstore
    conversation['conversation_chain'] = get_conversationchain(vectorstore)

def handle_question(question, conversation):
    response = conversation({'question': question})
    chat_history = response["chat_history"]
    for i, msg in enumerate(chat_history):
        if i % 2 == 0:
            print(f"User: {msg.content}")
        else:
            print(f"Bot: {msg.content}")

def main():
    conversation = {'conversation_chain': None}

    while True:
        print("1. Ask question")
        print("2. Process PDFs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            question = input("Enter your question: ")
            if question:
                handle_question(question, conversation['conversation_chain'])

        elif choice == "2":
            files = input("Enter PDF file paths separated by comma: ")
            files = files.split(",")
            try:
                process_pdf(files, conversation)
                print("PDF files processed successfully.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()
