from  langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path
# Obtén la ruta del directorio donde está tu script
directorio_actual = Path(__file__).parent
# Combina el directorio con el nombre de tu archivo PDF
ruta_pdf = directorio_actual / "pdf" / "terminalo.pdf"

print(f"contenido de ruta: {ruta_pdf}")
loader = PyMuPDFLoader(ruta_pdf)
print(f"\ncontenido de loader: {loader}")
documentos = loader.load()


print(f"\nimprimiendo la info de docuemnts: {documentos}") #: Esta línea imprime la lista de objetos Document completa


"""
El método load() le indica al cargador que comience a leer el PDF.
 El resultado es una lista de objetos llamados Document. Cada objeto Document  en la lista representa una página del PDF.

"""

# 'documents' es la lista de objetos Document cargados
total_paginas = len(documentos)
print(f"\nEl total de páginas del PDF es: {total_paginas}")

print("\n  -----haciendo el recorrido -----")
for iteracion, doc in enumerate(documentos, 1) :
    print(f"-- --- pagina {iteracion}\n{doc.page_content}\n {'-'*40}")