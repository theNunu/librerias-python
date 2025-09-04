
print(""" 
Ejemplo 6: Usar enumerate con una lista y modificar elementos
Puedes usar el índice para modificar elementos de una lista:

""")
numeros = [10, 20, 30, 50]

for indice, valor in enumerate(numeros):
    numeros[indice] = valor * 2

print(numeros)