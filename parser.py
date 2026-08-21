import pdfplumber

def extract_resume(uploaded_file):
    resume_text = ""
    total_pages = 0

    with pdfplumber.open(uploaded_file) as pdf:
        total_pages = len(pdf.pages)

        for page in pdf.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    return resume_text, total_pages