import time
import random


print("""   -------------------------------------------------------------------------------------------- 
            2. Implementación de una Lógica de Reintento con Retraso Progresivo ("Exponential Backoff")
            -------------------------------------------------------------------------------------------- 
      


""")
def conectar_a_servidor():
    """Simula una conexión a un servidor que puede fallar aleatoriamente."""
    if random.random() > 0.7:  # 30% de probabilidad de éxito
        print("¡Conexión exitosa!")
        return True
    else:
        print("Error: Conexión fallida.")
        return False

intentos_maximos = 5
tiempo_base_espera = 2  # Segundos

print("Intentando conectar al servidor...")

for intento in range(1, intentos_maximos + 1):
    print(f"\nIntento {intento} de {intentos_maximos}...")

    if conectar_a_servidor():
        print("¡Conexión establecida exitosamente!")
        break
    else:
        # Calcula el tiempo de espera, que se duplica en cada intento
        tiempo_espera = tiempo_base_espera ** intento  
        print(f"{tiempo_espera} = {tiempo_base_espera} al cuadrado de **{ intento}")
        print(f"Falló la conexión. Esperando {tiempo_espera} segundos para reintentar...")
        time.sleep(tiempo_espera)
else:
    # Este bloque 'else' se ejecuta si el bucle termina sin un 'break'
    print("\nNo se pudo conectar al servidor después de varios intentos. Saliendo.")