import time
def calcular_edad(edad):
    current_time = time.localtime()
    print(f"El año actual es: {current_time.tm_year}")
    print(f"El mes actual es: {current_time.tm_mon}")
    print(f"La hora actual es: {current_time.tm_hour}")
    
    return f"tu edad acual es {edad} años"