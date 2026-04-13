from typing import List
import PyPDF2
import os


def extract_text_from_pdf(pdf_path: str) -> List[str]:
    if not pdf_path:
        raise ValueError("The file path is empty. Please provide a valid path to the PDF file.")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file '{pdf_path}' was not found.")

    with open(pdf_path, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        text_content = []

        for page in reader.pages:
            content = page.extract_text()
            text_content.append(content if content is not None else "")

        return text_content


if __name__ == '__main__':
    # Replace 'pgb-smart FR-NL.pdf' with the actual path to your PDF file.
    extracted_text = extract_text_from_pdf('pgb-smart FR-NL.pdf')
    for text in extracted_text:
        print(text)





        