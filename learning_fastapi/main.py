from typing import Union
print("1")
from fastapi import FastAPI
print("2")
from learning_fastapi.mongo_db.conexion import connect_to_mongodb
print("3")
from learning_fastapi.mongo_db.champions_models import Champion
app = FastAPI()


def _get_collections():
    db, champions = connect_to_mongodb()
    return db, champions

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Serializador para convertir documentos de MongoDB a JSON
def champion_serializer(champion) -> dict:
    return {
        "id champion": str(champion["_id"]),
        "name champion": champion["name"],
        "carril champion": champion["carril"]
    }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/crear_campeones")
def crear_campeon(data: Champion):
    db, campeones = _get_collections()

    campeon_datos = {
        "name": data.name,
        "carril": data.carril
    }
    
    print(f"campeon datos {campeon_datos}")
    
    champion = campeones.insert_one(campeon_datos)
    
    print(f"champion: {champion}")
    print("\nel campeon se creo")
    return {"message": "Campeón creado", 
            "id": str(champion.inserted_id),
            "name del camepon": data.name,
            "carril del campeon": data.carril
            }
    
@app.get("/obtener_campeones", response_model=list[dict])
def obtener_todos_los_campeones():
    db, campeones = _get_collections()
    # Obtener todos los documentos de la colección
    champions = [champion_serializer(champ) for champ in campeones.find()]
    return champions
    
# @app.get("/campeon_id/{id}")
# def obtener_todos_los_campeones(data: Champion):
    
#     if not idCampeon == data.inserted_id:
        
#     db, campeones = connect_to_mongodb()
#     return {
#         "message": "obtenido campeon por id"
#     }

