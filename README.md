# bookReader
 epub and pdf reader

# Extract Text from EPUB and PDF

## 📌 Overview
This Python script extracts text from **EPUB** and **PDF** files and saves it as a `.txt` file in the same directory as the original document.

## 🚀 Features
- Supports **EPUB** and **PDF** formats.
- Automatically **detects file type** and applies the correct extraction method.
- Extracted text is **saved in a `.txt` file** in the same location as the input file.
- Uses **BeautifulSoup** to clean up HTML content in EPUB files.
- Handles **multi-page PDF documents** and extracts text efficiently.

## 🛠️ Requirements
Ensure you have the following Python libraries installed:
```sh
pip install ebooklib beautifulsoup4 pypdf
```

## 🔧 Usage
1. **Modify** the `file_path` variable in the script with the full path to your EPUB or PDF file.
2. **Run** the script:
```sh
python script.py
```
3. The extracted text will be saved as a `.txt` file in the same directory as the original document.

## 📂 Output Example
If your input file is:
```
C:/Users/andre/Projetos/books/sample.epub
```
The extracted text will be saved as:
```
C:/Users/andre/Projetos/books/sample.txt
```

## 📜 Code Breakdown
- `extract_text_from_epub(epub_file_path)`: Extracts and cleans text from EPUB files.
- `extract_text_from_pdf(pdf_file_path)`: Extracts text from PDF documents.
- `save_text_to_file(text, original_file_path)`: Saves extracted text into a `.txt` file.
- `extract_and_save(file_path)`: Determines file type, processes extraction, and saves the result.

## 🔗 Dependencies
- `ebooklib` (for EPUB handling)
- `beautifulsoup4` (for parsing HTML content in EPUBs)
- `pypdf` (for extracting text from PDF files)

## 📝 Notes
- Some PDFs contain scanned images instead of selectable text. This script does not support OCR (Optical Character Recognition). If you need OCR, consider using **Tesseract-OCR** (`pytesseract`).

## 🏆 Contributing
Feel free to improve this script by adding new features such as OCR support or additional file formats.

---
📧 Need help? Open an issue or reach out! 🚀

