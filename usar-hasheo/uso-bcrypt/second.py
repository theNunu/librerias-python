print(" --- USO COMPLEJO --- ")
import bcrypt
import time

password = b'complexpass'

for rounds in [10, 12, 14]:
    start = time.time()
    salt = bcrypt.gensalt(rounds=rounds)
    hashed = bcrypt.hashpw(password, salt)
    end = time.time()
    print(f'Rounds: {rounds}, Time: {end - start:.4f} seconds, Hashed: {hashed}')

# Salida de ejemplo (tiempos aproximados; variarán por hardware):
""" Explicación detallada: Cada +1 en rounds duplica el tiempo (exponencial). Para apps con muchos usuarios, 
elige rounds que tomen ~0.5-1 segundo por hash. Esto hace ataques caros (un atacante probaría miles de 
contraseñas por segundo en hardware simple). Usa time para benchmarkear en tu entorno.
"""