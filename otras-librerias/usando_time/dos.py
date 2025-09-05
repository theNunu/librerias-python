import time

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Formatted time:", formatted_time)


print("\n -- -- -- usando solo localtime -- -- --")
tiempo_local = time.localtime()

print(f"tiempo local: {tiempo_local}")
tiempo_formateado = time.strftime("%Y-%m-%d %H:%M:%S", tiempo_local)
print(f"tiempo formateado: {tiempo_formateado}")

local_time = time.localtime()
utc_time = time.gmtime()

print("Local time:", local_time)
print("UTC time:", utc_time)