
from hashear_password import hashear_con_hashlib, hashear_con_bcrypt


password = input("ingresa una contraseña: ")

result = hashear_con_hashlib(password)
print(f"la contraseña hasheada (hashlib) es: {result}")


other_result = hashear_con_bcrypt(password)
print(f"la contraseña hasheada (bcrypt) es: {other_result}")