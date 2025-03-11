import fitz

async def extract_text_from_pdf(file_content):
    text = ""
    pdf_document = fitz.open(stream=file_content, filetype="pdf")
    for page in pdf_document:
        text += page.get_text()
    return text