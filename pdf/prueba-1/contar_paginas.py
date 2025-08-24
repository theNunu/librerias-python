import pdfplumber
import os

ruta2 = "./pdf/prueba-1/pdfs/terminalo.pdf"

print("\n\n *** *** *** imprimiendo solo la primera pagina *** *** ***")

# with pdfplumber.open(ruta2) as temp:
#     first_page = temp.pages[2]
#     print(first_page.extract_text())

with pdfplumber.open(ruta2) as temp:
        print(f"\ntipo de dato: {type(temp)}")
            # Obtener el nombre del archivo sin la ruta de la carpeta
        nombre_archivo = os.path.basename(ruta2)
        print(f'nombre del archivo: {nombre_archivo}')
        numero_de_paginas = len(temp.pages)
        print(f"\nnumero de paginas: {numero_de_paginas}")
        pagina =  temp.pages[4]
        # print(pagina.extract_text())


file_name = os.path.basename(ruta2)

print(f"\n\n\n IMPRIMIR TODAS LAS PAGINAS DEL ARCHIVO {file_name}: ")

with pdfplumber.open(ruta2) as pdf:
        numero_de_paginas = len(pdf.pages)
        print(f"\nnumero de paginas: {numero_de_paginas}")


      # Iterar a través de cada página
        for i, pagina in enumerate(pdf.pages):
                # Extraer el texto de la página actual
                texto = pagina.extract_text()
                
                # Imprimir el encabezado con el número de página y el nombre del archivo
                print(f"--- Página {i + 1} de {numero_de_paginas} del archivo: {file_name} ---")
                
                # Imprimir el texto de la página
                if texto:
                    print(texto)
                else:
                    print("La página no tiene texto o no es legible.")
                
                print("-" * 50)  # Separador para mayor claridad



