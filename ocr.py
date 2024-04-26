import pytesseract as tess
from PIL import Image, ImageTk
import tkinter as tk
import os

# Set Tesseract executable and TESSDATA_PREFIX
tess.pytesseract.tesseract_cmd = r'C:\Users\borha\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Users\borha\AppData\Local\Programs\Tesseract-OCR\tessdata'

# Load Arabic text image
image = Image.open('utopia.png')

# Perform OCR
arabic_text = tess.image_to_string(image, lang='ara')

# Create Tkinter window
window = tk.Tk()
window.title("Arabic OCR Result")

# Create a label to display the text
text_label = tk.Label(window, text=arabic_text, font=("Arial", 12), wraplength=600, justify="right")
text_label.pack(padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
