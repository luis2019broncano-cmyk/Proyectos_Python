#UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
#Estudiante: Luis Broncano
#Fecha: 23/04/2026
#Asignatura: Metodos Numericos
############MEJORA DE ARCHIVO##############

import math

# =================================================
# Definición de Funciones
# =================================================

def calcular_media(datos):
    """Calcula la media aritmética (suma de datos / n)."""
    suma = sum(datos)
    n = len(datos)
    return suma / n

def calcular_varianza_poblacional(datos):
    """Calcula la varianza poblacional dividiendo para N."""
    m = calcular_media(datos)
    suma_cuadrados = sum((x - m) ** 2 for x in datos)
    return suma_cuadrados / len(datos)

def calcular_varianza_muestral(datos):
    """Calcula la varianza muestral dividiendo para N-1."""
    n = len(datos)
    if n < 2:
        return 0 # Manejo de error si no hay suficientes datos
    m = calcular_media(datos)
    suma_cuadrados = sum((x - m) ** 2 for x in datos)
    return suma_cuadrados / (n - 1)

def calcular_desviacion_estandar(datos, tipo='poblacional'):
    """Calcula la raíz cuadrada de la varianza seleccionada."""
    if tipo == 'poblacional':
        v = calcular_varianza_poblacional(datos)
    else:
        v = calcular_varianza_muestral(datos)
    return math.sqrt(v)

def estadistica_completa(datos):
    """
    Función que llama a todos los cálculos y muestra un reporte 
    formateado. (Punto 2: Función completa).
    """
    # Manejo de errores: verifica si el vector está vacío
    if not datos:
        print("Error: El conjunto de datos está vacío.")
        return

    # Realización de cálculos
    promedio = calcular_media(datos)
    var_pob = calcular_varianza_poblacional(datos)
    var_mue = calcular_varianza_muestral(datos)
    desv_pob = calcular_desviacion_estandar(datos, 'poblacional')
    desv_mue = calcular_desviacion_estandar(datos, 'muestral')

    # Reporte formateado
    print("\n" + "="*50)
    print("          REPORTE ESTADÍSTICO COMPLETO")
    print("="*50)
    print(f"Total de elementos:          {len(datos)}")
    print(f"Media aritmética:            {promedio:.4f}")
    print("-" * 50)
    print(f"Varianza Poblacional:        {var_pob:.4f}")
    print(f"Varianza Muestral:           {var_mue:.4f}")
    print("-" * 50)
    print(f"Desviación Estándar (Pob):   {desv_pob:.4f}")
    print(f"Desviación Estándar (Mue):   {desv_mue:.4f}")
    print("="*50)

# =================================================
# Programa Principal
# =================================================

def main():
    print("==================================================")
    print("Estadística Descriptiva - Sistema de Análisis")
    print("==================================================")

    # Manejo de errores al ingresar cantidad
    try:
        cantidad_str = input("¿Cuántos números desea ingresar? ")
        cantidad = int(cantidad_str)
        
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número entero positivo.")
            return

        numeros = []
        for i in range(cantidad):
            valor = float(input(f"Número {i + 1}: "))
            numeros.append(valor)

        # Llamada a la función unificada
        estadistica_completa(numeros)

    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese solo números.")

if __name__ == "__main__":
    main()