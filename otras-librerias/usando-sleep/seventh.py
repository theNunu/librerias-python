import time
print("""   -----------------------------------
            Control de Tasa de Solicitudes a una API
            -----------------------------------
""")
def hacer_solicitud_api(numero_solicitud):
    """Simula una solicitud a una API y muestra su número."""
    print(f"Haciendo solicitud número {numero_solicitud} a la API...")
    # Aquí iría el código real para llamar a la API
    print(f"Solicitud {numero_solicitud} completada.")

limite_solicitudes_por_minuto = 60
tiempo_espera_entre_solicitudes = 60 / limite_solicitudes_por_minuto  # 1 segundo

print("Iniciando envío de solicitudes a la API con control de tasa...")

for i in range(1, 11):  # Haremos 10 solicitudes# inicia en el 1, finaliza en 11(10)
    hacer_solicitud_api(i)
    # Esperamos el tiempo necesario para no exceder el límite
    time.sleep(1)

print("\nEnvío de solicitudes finalizado.")