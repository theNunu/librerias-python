import pdfplumber

# Asegúrate de que esta ruta sea la correcta para tu archivo PDF
ruta1 = "/pdf/prueba-1/pdfs/terminalo.pdf"

try:
    # Abre el archivo PDF usando pdfplumber.open()
    with pdfplumber.open(ruta1) as lector_pdf:
        # Itera sobre todas las páginas del documento
        for num_pagina in range(len(lector_pdf.pages)):
            pagina = lector_pdf.pages[num_pagina]
            texto = pagina.extract_text()
            
            # Imprime el texto de cada página
            if texto:
                print(f"--- Contenido de la página {num_pagina + 1} ---")
                print(texto)
            else:
                print(f"--- La página {num_pagina + 1} no contiene texto extraíble ---")

except FileNotFoundError:
    print(f"Error: El archivo no se encontró en la ruta '{ruta1}'")
except Exception as e:
    print(f"Ocurrió un error al leer el PDF: {e}")