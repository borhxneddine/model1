import PyPDF2
import re
import tkinter as tk
from tkinter import scrolledtext

def extract_arabic_text(pdf_path):
    arabic_text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            # Filter out non-Arabic characters using a regular expression
            arabic_text += re.sub(r'[^\u0600-\u06FF\s]', '', page_text)
    return arabic_text

def display_arabic_text(pdf_path):
    arabic_text = extract_arabic_text(pdf_path)
    
    # Create Tkinter window
    window = tk.Tk()
    window.title("Arabic Text Extractor")
    
    # Create a scrolled text widget to display the Arabic text
    text_area = scrolledtext.ScrolledText(window, width=80, height=20, font=("Arial", 12))
    text_area.insert(tk.INSERT, arabic_text)
    text_area.pack(expand=True, fill='both')
    
    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    pdf_path = 'BAC_2021.pdf'  # Path to your PDF file
    display_arabic_text(pdf_path)
