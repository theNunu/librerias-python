frutas = ["manzana", "banana", "naranja"]

for indice, valor in enumerate(frutas, 1):
    print(f"Índice: {indice}, Valor: {valor}")
    
    
    
print("\n  ---- ----- OTRO EJEMPLO ---- ----")
print("\nEjemplo 4: Iterar sobre una cadena")
texto = "Hola"

for indice, caracter in enumerate(texto, 1):
    print(f"Posición {indice}: {caracter}")
    
print("\n ------   ----- Ejemplo 5: Combinar con una lista de tuplas")

parejas = [("Ana", 25), ("Luis", 30), ("María", 28)] #lista = [], tupla = ()

for indice, (nombre, edad) in enumerate(parejas, start=1):
    print(f"{indice}. {nombre} tiene {edad} años")