from  langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path
# Obtén la ruta del directorio donde está tu script
directorio_actual = Path(__file__).parent
# Combina el directorio con el nombre de tu archivo PDF
ruta_pdf = directorio_actual / "pdf" / "La_llegada_de_Ana.pdf"

print(f"contenido de ruta: {ruta_pdf}")
loader = PyMuPDFLoader(ruta_pdf)
print(f"\ncontenido de loader: {loader}")
documentos = loader.load()


print(f"\nimprimiendo la info de docuemnts: {documentos}") #: Esta línea imprime la lista de objetos Document completa


# 'documents' es la lista de o# Accediendo a la metadata de la primera página (índice 0)
meta_primera_pagina = documentos[0].metadata

# Imprimir el diccionario de metadatos de la primera página
print(f"Metadata de la primera página: {meta_primera_pagina}")

# Puedes acceder a valores específicos, por ejemplo, el número de página
numero_de_pagina = documentos[0].metadata['page']
print(f"Número de la primera página: {numero_de_pagina}")

# En la metadata también se guarda la fuente (el nombre del archivo)
fuente_del_documento = documentos[0].metadata['source']
print(f"Fuente del documento: {fuente_del_documento}")
print("")
total_paginas = len(documentos)
print(f"\nEl total de páginas del PDF es: {total_paginas}")

print("\n  -----haciendo el recorrido -----")
for iteracion, doc in enumerate(documentos, 1) :
    print(f"-- --- pagina {iteracion}\n{doc.page_content}\n {'-'*40}")