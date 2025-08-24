import pdfplumber
import os

ruta = "./pdf/prueba-1/pdfs/mishi.pdf"

# with pdfplumber.open() as temp:
#     first_page = temp.pages[0]
#     print(first_page.extract_text())


# Abrir el archivo PDF
with pdfplumber.open(ruta) as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        print(texto)


