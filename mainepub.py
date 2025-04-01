from ebooklib import epub
from bs4 import BeautifulSoup  # Para extrair o texto corretamente de HTML

# Caminho do arquivo EPUB
epub_file_path = r"C:\Users\andre\Projetos\extracTextfromBook\books\Transformando Suor em Ouro - Bernardo Rocha de Rezende-1.epub"

def extract_text_from_epub(epub_file_path):
    book = epub.read_epub(epub_file_path)
    text = ''
    
    for item in book.get_items():
        if item.get_type() == 9:  # 9 representa documentos XHTML no ebooklib
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text() + '\n'
    
    return text

# Executa a extração
text = extract_text_from_epub(epub_file_path)
print(text)
