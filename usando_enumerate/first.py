
nombres = ["walter", "skyler", "jesse", "gustavo", "eduardo", "tuco"]
print(" -- recorrido normal de nombres:")
for n in nombres:
    print(n)

print("-+-" * 20)

print(" -----   usando enumerate -----")
for n in enumerate(nombres, 1): # lo que se itera
    print(n)