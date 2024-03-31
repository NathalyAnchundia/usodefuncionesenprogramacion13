def temp_promedio(ciudades_temperaturas):
# Inicializamos  un diccionario vacío llamado “temperaturas_promedio”
# para almacenar las temperaturas promedio de cada ciudad.
    temperaturas_promedio = {}
#Iteramos a través de cada ciudad y sus temperaturas correspondientes en el diccionario de entrada.
    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio
    return temperaturas_promedio # Devuelve el diccionario “temp_promedio”.
#se define un diccionario de control con tres ciudades y temperaturas
control = {"ambato": [26, 25, 25, 28, 24,26],
           "quevedo": [18, 20, 15, 16, 20,19,18],
           "manabi": [21, 15, 20, 19, 18,18,13]}
temperaturas_promedio = temp_promedio(control)
print("Temperaturas Promedio de ciudades:")
for ciudad, promedio in temperaturas_promedio.items():
# Imprime el nombre de la ciudad y su temperatura promedio con 1 float
    print(f"{ciudad}: {promedio:.1f}°C")