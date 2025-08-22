import jwt
JWT_SECRET = "JWT_SECRET"
JWT_ALGORITHM = "HS256" 

def crear_acceso_token(id_user:str, name_user: str, last_name_user: str, password_user: str, age_user:int)-> str:
    payload = {
        "id del usuario": id_user,
        "nombre del usuario": name_user,
        "apellido del usuario": last_name_user,
        "contraseña del usuario": password_user,
        "edad del usuario": age_user
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM )

def deshacer_token(token: str)-> str:
    return jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
