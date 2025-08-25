import pdfplumber
import os

archivo_pdf = "/pdf/prueba-1/pdfs/terminalo.pdf"
def leer_pdf(archivo_pdf: str) -> str:
    # Obtener el nombre del archivo de la ruta
    file_name = os.path.basename(archivo_pdf)
    texto_completo = ""  # Variable para almacenar todo el texto del PDF

    try:
        with pdfplumber.open(archivo_pdf) as pdf:
            numero_de_paginas = len(pdf.pages)
            print(f"Número de páginas en '{file_name}': {numero_de_paginas}\n")

            # Iterar a través de cada página
            for i, pagina in enumerate(pdf.pages):
                # Extraer el texto de la página actual
                texto = pagina.extract_text()
                
                # Encabezado para la terminal
                print(f"--- Página {i + 1} de {numero_de_paginas} del archivo: {file_name} ---")
                
                # Imprimir y acumular el texto de la página
                if texto:
                    print(texto)
                    texto_completo += texto + "\n"
                else:
                    print("La página no tiene texto o no es legible.")
                
                print("-" * 50)
    except FileNotFoundError:
        return f"❌ Error: El archivo '{archivo_pdf}' no se encontró."
    except Exception as e:
        return f"❌ Ocurrió un error al procesar el archivo PDF: {e}"

    return texto_completo # Retorna todo el texto del PDF

# --- Ejemplo de uso ---
ruta = "./pdfs/libro.pdf" # Asegúrate de que esta ruta sea correcta
result = leer_pdf(ruta)
print("\n--- Texto completo del PDF (retorno de la función) ---")
print(result)