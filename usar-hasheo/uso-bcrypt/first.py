import bcrypt

password = b'supersecret'  # Contraseña como bytes (usa b'' para literales) SI LE QUITAS B DARA ERROR

salt = bcrypt.gensalt()  # Genera sal con rondas default (12)

hashed = bcrypt.hashpw(password, salt)  # Hashea

print(f'Salt: {salt}')
print(f'Hashed: {hashed}')
print(f"deberia lanzar true: {bcrypt.checkpw(password, hashed)}")

"""  
Explicación detallada: La sal es aleatoria y se usa para "salpimentar" 
la contraseña. El hash resultante es único cada vez 
(incluso para la misma contraseña, por la sal)
"""

print("  *****  Verificar una contraseña contra un hash:   *****  ")

import bcrypt

my_password = b'alexkiller04'

# Generamos un hash para demo (en real, lo cargas de DB)
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(my_password, salt)

print(f'Hashed: {hashed}')
print(f'Check correct: {bcrypt.checkpw(my_password, hashed)}')
print(f'Check wrong: {bcrypt.checkpw(b'wrong', hashed)}')

"""  
checkpw toma la contraseña, extrae la sal del hash, la hashea internamente y compara.
 Es seguro contra timing attacks (no revela info por tiempo). Úsalo en logins para validar sin exponer la contraseña.
"""