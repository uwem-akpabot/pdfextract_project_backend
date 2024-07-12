import fitz  # PyMuPDF
import spacy
from .models import PDFFile

nlp = spacy.load('en_core_web_sm')

def extract_and_process_pdf(pdf_path, pdf_instance):
    # Extract text from the PDF
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    # Process text to identify nouns and verbs
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ == 'NOUN']
    verbs = [token.text for token in doc if token.pos_ == 'VERB']

    # Update the PDFFile instance with the extracted content
    pdf_instance.content = text
    pdf_instance.nouns = nouns
    pdf_instance.verbs = verbs
    pdf_instance.save()
