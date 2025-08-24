

def hashear_con_hashlib(password: str) -> str:
    print(f"contraseña ingresada: {password}")

    import hashlib
    password_got_byte = password.encode("utf-8")

    hash256 = hashlib.sha256()

    hash256.update(password_got_byte)
    contrasena_hasheada = hash256.hexdigest()
    print(f"password con hashlib es de tipo {type(contrasena_hasheada)}")

    return contrasena_hasheada


def hashear_con_bcrypt(password: str) -> str:
    print(f"\ncontraseña ingresada: {password}")
    import bcrypt

    password_byteada = password.encode("utf-8")
    salt_creada = bcrypt.gensalt()

    password_hasheada = bcrypt.hashpw(password_byteada, salt_creada)
    print(f"password con bcrypt es de tipo {type(password_hasheada)}")
    # password_become_str = str(password_byteada)
    # print(f"\ncontraseña convertida a str {password_become_str}")
    # print(f"tipo de dato: {type(password_become_str)}")

    return password_hasheada



