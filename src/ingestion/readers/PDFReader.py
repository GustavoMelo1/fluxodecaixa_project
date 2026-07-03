import pdfplumber
from .base import BaseReader

class PDFReader(BaseReader):
    def read(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            texto = [pagina.extract_text() for pagina in pdf.pages]
        return texto