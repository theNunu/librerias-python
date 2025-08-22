mi_contrasena = "alexis2004"


def hashear_password(password: str)-> str:
    import hashlib
    # hash_obj = hashlib.sha256(password.encode('utf-8'))
    # print(f'antes del hexdigest: {hash_obj}')
    encode_password = password.encode("utf-8")
    print(f"password recien encodeado: {encode_password}")
    hash256 = hashlib.sha256()
    hash256.update(encode_password)
    print(f"encode_password luego del update {encode_password}")
    hashed_password = hash256.hexdigest()
    return hashed_password

    
result = hashear_password(mi_contrasena)

print(f'la contrseña hasheada: {result}')
print(f'la contrseña hasheada: {len(result)}')
# import hashlib

# def generar_hash(texto: str) -> str:
#     if not isinstance(texto, str):
#         raise ValueError("El input debe ser un string")
    
#     # Convertir el string a bytes y generar el hash
#     hash_obj = hashlib.sha256(texto.encode('utf-8'))
#     return hash_obj.hexdigest()


    # encode_password = plain_password.encode("utf-8")
    # hash256 = hashlib.sha256()
    # hash256.update(encode_password)
    # hashed_password = hash256.hexdigest()
    # return hashed_password
