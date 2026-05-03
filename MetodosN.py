#UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
#Estudiante: Luis Broncano
#Fecha: 23/04/2026
#Asignatura: Metodos Numericos
# Ejercicio 5: Programa Principal y Validacion
############# Ejercicio 3.2. PYTHON #############


import math

# =================================================
# Definición de Funciones
# =================================================

def calcular_media(datos):
    suma = 0
    n = len(datos)
    for valor in datos:
        suma += valor
    return suma / n

def calcular_varianza_poblacional(datos):
    m = calcular_media(datos)
    suma_cuadrados = 0
    n = len(datos)
    for valor in datos:
        diferencia = valor - m
        suma_cuadrados += diferencia**2
    return suma_cuadrados / n

def calcular_varianza_muestral(datos):
    n = len(datos)
    # Evitamos división por cero si solo hay un dato
    if n < 2:
        return 0
    
    m = calcular_media(datos)
    suma_cuadrados = 0
    for valor in datos:
        diferencia = valor - m
        suma_cuadrados += diferencia**2
    return suma_cuadrados / (n - 1)

def calcular_desviacion_estandar(datos, tipo='poblacional'):
    if tipo == 'poblacional':
        v = calcular_varianza_poblacional(datos)
    else:
        v = calcular_varianza_muestral(datos)
    # Raíz cuadrada
    return v**0.5

# =================================================
# Programa Principal
# =================================================

def main():
    print("==================================================")
    print("Estadistica descriptiva")
    print("==================================================")

    # Ingreso de datos
    print("\nIngrese numeros: ")
    try:
        numeros = []
        for i in range(5):
            valor = float(input(f"Número {i + 1}: "))
            numeros.append(valor)

        print("============================================")
        print("ESTADISTICA DESCRIPTIVA")
        print("============================================")
        print(f"Datos ingresados: {numeros}")
        print(f"Numero de elementos: {len(numeros)}\n")

        promedio = calcular_media(numeros)
        print(f"MEDIA: {promedio:.2f}\n")

        var_pob = calcular_varianza_poblacional(numeros)
        print(f"VARIANZA POBLACIONAL: {var_pob:.2f}")

        var_mue = calcular_varianza_muestral(numeros)
        print(f"VARIANZA MUESTRAL: {var_mue:.2f}\n")

        desv_pob = calcular_desviacion_estandar(numeros, 'poblacional')
        print(f"DESVIACION ESTANDAR POBLACIONAL: {desv_pob:.2f}")

        desv_mue = calcular_desviacion_estandar(numeros, 'muestral')
        print(f"DESVIACION ESTANDAR MUESTRAL: {desv_mue:.2f}")
        print("============================================")

    except ValueError:
        print("Error: Por favor, ingrese solo números válidos.")

if __name__ == "__main__":
    main()