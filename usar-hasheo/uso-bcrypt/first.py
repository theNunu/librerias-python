import bcrypt

password = b'supersecret'  # Contraseña como bytes (usa b'' para literales) SI LE QUITAS B DARA ERROR

salt = bcrypt.gensalt()  # Genera sal con rondas default (12)

hashed = bcrypt.hashpw(password, salt)  # Hashea

print(f'Salt: {salt}')
print(f'Hashed: {hashed}')