import hashlib

def doing_hash(contrasena: str) ->str:
    
    encode_contrasena = contrasena.encode("utf-8")
    hash_256 = hashlib.sha256()
    hash_256.update(encode_contrasena)
    contrasena_hasheada = hash_256.hexdigest()
    # print(f"tipo de dato de la contraseña hasheada: {type(contrasena_hasheada)}")
    
    return contrasena_hasheada
    