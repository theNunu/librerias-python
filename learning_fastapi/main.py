from typing import Union
print("1")
from fastapi import FastAPI
print("2")
from learning_fastapi.mongo_db.conexion import connect_to_mongodb
print("3")
from learning_fastapi.mongo_db.champions_models import Champion
from typing import List
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
        "message": "campeon obtenido: ",
        "id champion": str(champion["_id"]), #Convierte el ObjectId en una cadena (str(champion["_id"])).
        "name champion": champion["name"],
        "carril champion": champion["carril"]
    }


@app.post("/crear_campeon")
def crear_campeon(data: Champion):
    db, campeones = _get_collections()
    
    champions_mongo = campeones

    campeon_datos = {
        "name": data.name,
        "carril": data.carril
    }
    
    print(f"campeon datos {campeon_datos}")
    
    champion = champions_mongo.insert_one(campeon_datos)
    
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
    # champions = []
    # for champ in campeones.find():
    #     champions.append(champion_serializer(champ))
    
    
    return champions

@app.get("/mostrar_junglas")
def get_only_jungles():
    db, campeones = _get_collections()
    champions = [champion_serializer(champ) for champ in campeones.find( {"carril": "jungla"} )] 
    print(f"\nsolo junglas: {champions}")
    return champions

# @app.get("obtener_by_id")
# def get_only_by_id(id_campeon):
#     db, campeones = _get_collections()
#     champions = [champion_serializer(champ) for champ in campeones.find_one({"id": id_campeon} )] 
#     print(f"\nsolo  id: {champions}")
#     return champions


@app.get("/obtener_campeones3", response_model=List[Champion])
def obtener_todos_los_campeones():
    db, campeones = _get_collections()
    champions = [Champion(id=str(champ["_id"]), name=champ["name"], carril=champ["carril"]) for champ in campeones.find()]
    print(f"\ninfo de Champions: {champions} \n")
    print(f"contenido de Champion: {Champion}")
    return champions