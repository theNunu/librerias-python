print(""" 
Ejemplo 7: Ignorar el valor con _
Si solo necesitas el índice y no el valor, puedes usar _ para ignorar el segundo elemento:

""")

colores = ["rojo", "verde", "azul"]

for indice, _ in enumerate(colores):
    print(f"Índice: {indice}")


print("""  \n
Ejemplo 8: Usar enumerate con range para personalizar iteraciones
Puedes combinar enumerate con range para iterar sobre un rango personalizado:



""")
for indice, _ in enumerate(range(5, 10), start=1):
    print(f"Índice: {indice}")


print("\n -- UN RECORRIDO CUALQUIERA")
for indice, _ in enumerate(range(5, 16), 1): #range = inicio , final, cantidad numerica de saltos
    print(f"indice: {indice}")



print("\n --- --- Ejemplo 10: Usar con una lista de diccionarios --- --- ")
print("Si trabajas con una lista de diccionarios, puedes acceder a los índices y los datos:")

personas = [{"nombre": "Juan", "edad": 25}, {"nombre": "Pedro", "edad": 30}]

for i, persona in enumerate(personas, start=1):
    print(f"{i}. {persona['nombre']} - Edad: {persona['edad']}") 