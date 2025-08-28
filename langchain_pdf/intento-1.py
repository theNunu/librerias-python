from  langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path
libro1 = "pdf/new_gato.pdf"
#ruta_temporal = f"./temp_{file.filename}
    
# Verificar que el archivo existe
# Verificar que el archivo existe
if not Path(libro1).exists():
    raise FileNotFoundError(f"El archivo {libro1} no se encuentra en la ruta especificada.")

loader = PyMuPDFLoader(libro1)
documents = loader.load()

for i, doc in enumerate(documents, 1):
    print(f"Página {i}:\n{doc.page_content}\n{'-'*40}")
    
# def leer_pdf(path: Path) -> str:
#     try:
#         loader = PyMuPDFLoader(str(path))
#         documents = loader.load()
#         print(f"imprimiendo el documents {documents}  \n")
     
#         texto = "\n".join(doc.page_content for doc in documents)
#         print(f"imprimiendo texto: {texto}")
        
#         return texto.strip()
#     except Exception as e:
#         raise Exception(f"Error al leer el PDF: {str(e)}")