from security.jwt import crear_acceso_token, deshacer_token
from security.hashear import doing_hash
import uuid

nombre_usuario = "alexis"
apellido_usuario = "cepeda"
contrasena_usuario = "alexis12345"
id_usuario = str(uuid.uuid4())
edad_usuario = 21


mi_usuario = {
    "id": id_usuario,
    "contraseña": doing_hash(contrasena_usuario),
    "edad": edad_usuario,
}

"""
 **** el usuario recorrido(clave, valor): **** 
id: c3db31df-62ec-4ee4-82e2-de7fa52af97a
contraseña: 9421a4413e7762f379d7ffbb6fb6441110e974b9c29f4cc5fb1d9f5bdaa70afe
edad: 21 
"""

print(mi_usuario)
print("\n **** el usuario recorrido(clave, valor): **** ")
for c, v in mi_usuario.items():
    print(f"{c}: {v}")


token_creado = crear_acceso_token(
    id_user=id_usuario, password_user=contrasena_usuario, age_user=edad_usuario
)

print(f"\ntoken creado: {token_creado}")
print(
    f"\ntipo de dato del token creado(a pesar de tener edad como int): {type(token_creado)}"
)
print(f"longitud del token: {len(token_creado)}")

token_desechado = deshacer_token(token_creado)

print(f"token convertido otra vez a lista: {token_desechado}")


# print("\nHASHEAR CONTRASEÑA:")
# hashed_password = doing_hash(contrasena_usuario)
# print(hashed_password)
# print(f"tipo de dato de la contraseña hasheada: {type(hashed_password)}")
