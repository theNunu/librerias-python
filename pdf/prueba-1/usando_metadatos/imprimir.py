import pdfplumber

# Asegúrate de que esta ruta sea la correcta para tu archivo PDF
ruta1 = "../pdfs/terminalo.pdf"
print(ruta1)

try:
    with pdfplumber.open(ruta1) as temp:
        # Itera sobre cada página en el documento
        for page in temp.pages:
            # Extrae el texto de la página actual y lo imprime
            print(f"--- Texto de la página {page.page_number} ---")
            print(page.extract_text())
            print("---------------------------------------")
            
except FileNotFoundError:
    print(f"Error: El archivo no se encontró en la ruta '{ruta1}'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")