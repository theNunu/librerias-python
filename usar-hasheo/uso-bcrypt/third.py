"""  
es para hashing unidireccional, ideal para contraseñas.
bcrypt
Fácil de usar: Integra bien con apps web (ej. Flask, Django) para autenticación.


"""
import bcrypt
password = "la formula secreta"
print(f' password original: {password}')
print(f"el tipo de dato del password {type(password)}")
password_byteada = password.encode("utf-8")
print(f'\npasword byteada: {password_byteada}')

print(f"el tipo de dato del password byteada {type(password_byteada)}")
salt_creada = bcrypt.gensalt()
print(f"\nsalt creada {salt_creada}")

password_bcrypt = bcrypt.hashpw(password_byteada, salt_creada)
print(f"contraseña creada {password_bcrypt}")