import os
from ebooklib import epub
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# Caminho do arquivo
file_path = r"C:\Users\andre\Projetos\extracTextfromBook\books\Stonehenge - Bernard Cornwell.epub"

def extract_text_from_epub(epub_file_path):
    """Extrai texto de um arquivo EPUB"""
    book = epub.read_epub(epub_file_path)
    text = ''

    for item in book.get_items():
        if item.get_type() == 9:  # 9 representa documentos XHTML no ebooklib
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text() + '\n'
    
    return text

def extract_text_from_pdf(pdf_file_path):
    """Extrai texto de um arquivo PDF"""
    reader = PdfReader(pdf_file_path)
    text = ''

    for page in reader.pages:
        text += page.extract_text() + '\n' if page.extract_text() else ''
    
    return text

def save_text_to_file(text, original_file_path):
    """Salva o texto extraído em um arquivo .txt no mesmo local do original"""
    base_name = os.path.splitext(original_file_path)[0]  # Remove a extensão original
    txt_file_path = base_name + ".txt"

    with open(txt_file_path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"Texto salvo em: {txt_file_path}")

def extract_and_save(file_path):
    """Determina o tipo do arquivo, extrai o texto e salva em um .txt"""
    if file_path.lower().endswith(".epub"):
        text = extract_text_from_epub(file_path)
    elif file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        print("Formato de arquivo não suportado.")
        return
    
    save_text_to_file(text, file_path)

# Executa a extração e salva em .txt
extract_and_save(file_path)
