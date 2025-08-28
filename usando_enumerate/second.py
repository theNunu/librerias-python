texto = ("""    enumerate es una función incorporada en Python que te permite iterar sobre una secuencia 
    como una lista, tupla o cadena) mientras también llevas un conteo automático del índice de cada elemento.
    Es muy útil cuando necesitas tanto el índice como el valor de los elementos durante un bucle, sin tener que 
    manejar manualmente un contador.""")

print(f"contenido de texto: {texto}")

result = texto.split()
print(f" imprimiendo texto en pedazos: {result}")

for i,r in enumerate(result, 1 ):
    # print(r)
    print(f" {i}: {r}")

# r_list = list(r)
# print(f"se convirtio a lista : {r_list}")

# word = "parola de la donne"
# print(word)
# new_word = word.split()
# print(new_word)