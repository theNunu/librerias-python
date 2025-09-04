from  langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path
# Obtén la ruta del directorio donde está tu script
directorio_actual = Path(__file__).parent
# Combina el directorio con el nombre de tu archivo PDF
ruta_pdf = directorio_actual / "pdf" / "El_triunfo_ de_Yahir.pdf"

# Verificar que el archivo existe
if not Path(ruta_pdf).exists():
    raise FileNotFoundError(f"El archivo {ruta_pdf} no se encuentra en la ruta especificada.")

loader = PyMuPDFLoader(ruta_pdf)
documents = loader.load()
print(f"imprimiendo la info de docuemnts: {documents}")
# print(f"formato del pdf: {documents.format}")

print("\n --- --- iniciando el recorrido --- ----")
for i, doc in enumerate(documents, 1):
    print(f"Página {i}:\n{doc.page_content}\n{'-'*40}")
    # print(f"formato del pdf: {doc.format}")
    
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