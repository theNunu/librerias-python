
import time
names = ["walter", "jesse", "saul", "skyler", "gustavo"]

print(f"contenido de names: {names}")

print("\n---- usando los recorridos (usando sleep)----")

for name in names:
    print(name)
    time.sleep(0.5)



print('\n -----   ejecucion NO  inmediata   -------')

for letra in '¡hola, mundo!':
    time.sleep(1)  # espera 2 segundos entre cada print()
    print(letra)

