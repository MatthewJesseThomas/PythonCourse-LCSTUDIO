import pyttsx3
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from io import StringIO


def speak_text(text):
    audio_book_reader = pyttsx3.init()
    audio_book_reader.say(text)
    audio_book_reader.runAndWait()


pdf_path = './pdf/es6_tutorial.pdf'

try:
    with open(pdf_path, 'rb') as book:
        resource_manager = PDFResourceManager()
        text_stream = StringIO()
        laparams = None
        device = TextConverter(resource_manager, text_stream, laparams=laparams)
        interpreter = PDFPageInterpreter(resource_manager, device)

        for page in PDFPage.get_pages(book):
            interpreter.process_page(page)

        text = text_stream.getvalue()

        num_pages = text.count('\f') + 1

        if num_pages == 0:
            print("No pages found in the PDF.")
        elif num_pages == 1:
            print("Only one page found in the PDF.")
        else:
            print(f"{num_pages} pages found in the PDF.")
            speak_text(f"There are {num_pages} pages in this audio book.")

        page_number = 1  # Specify the desired page number here (zero-based index)

        if 0 <= page_number < num_pages:
            pages = text.split('\f')
            page_text = pages[page_number]
            speak_text(page_text)
        else:
            print("Invalid page number.")

except FileNotFoundError:
    print("PDF file not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

def shutdown_procedure():
    shutdown_program = True
    