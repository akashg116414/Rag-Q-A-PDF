import fitz

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a given PDF file.
    
    :param pdf_path: Path to the PDF file
    :return: Extracted text as a string
    """
    try:
        with fitz.open(pdf_path) as doc:
            text = "\n".join([page.get_text("text") for page in doc])
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
