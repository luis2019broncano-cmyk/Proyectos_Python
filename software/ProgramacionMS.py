import serial
import time
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. CONFIGURACIÓN DEL PUERTO SERIAL
# ==========================================
# CAMBIAR EL PUERTO SEGÚN EL PUERTO QUE SE INGRESO
PUERTO = 'COM3' 
BAUDIOS = 115200 

try:
    esp32 = serial.Serial(PUERTO, BAUDIOS, timeout=1)
    print(f" Conectado exitosamente al ESP32 en {PUERTO}")
    time.sleep(2) # Esperar a que la conexión se estabilice
except Exception as e:
    print(f" Error al conectar: {e}")
    exit()

# ==========================================
# 2. VARIABLES DE CALIBRACIÓN Y DATOS
# ==========================================
muestras = 100 # Cantidad de datos a leer de golpe para formar la onda
voltajes = np.zeros(muestras)
corrientes = np.zeros(muestras)

# ==========================================
# 3. LECTURA Y PROCESAMIENTO
# ==========================================
print("Iniciando captura de datos...")

try:
    # Limpiamos basura del puerto antes de empezar
    esp32.flushInput() 
    
    for i in range(muestras):
        # Leer línea enviada por el ESP32 (Ejemplo esperado: "1800,2048\n")
        linea = esp32.readline().decode('utf-8').strip()
        
        if "," in linea:
            v_crudo, i_crudo = linea.split(",")
            
            # Convertir valor de ADC (0-4095) a Voltaje real (aprox)
            # Nota: Estos factores se ajustan calibrando tus sensores
            voltajes[i] = (float(v_crudo) - 1800) * 0.1  # Eliminando el offset
            corrientes[i] = (float(i_crudo) - 2048) * 0.05 # Eliminando el offset

    # ==========================================
    # 4. CÁLCULO DE IMPEDANCIA COMPLEJA
    # ==========================================
    # Calculamos valores RMS (Eficaces)
    v_rms = np.sqrt(np.mean(voltajes**2))
    i_rms = np.sqrt(np.mean(corrientes**2))
    
    # Simulaci+on de cálculo de ángulo (desfase)...
    fase_rad = np.radians(30) 
    
    # Identidad de Euler para formar el número complejo de la Impedancia (Z = R + jX)
    Z = (v_rms / i_rms) * (np.cos(fase_rad) + 1j * np.sin(fase_rad))
    
    print("\n--- RESULTADOS MECATRÓNICOS ---")
    print(f"Voltaje RMS: {v_rms:.2f} V")
    print(f"Corriente RMS: {i_rms:.2f} A")
    print(f"Impedancia Compleja (Z): {Z.real:.2f} + {Z.imag:.2f}j Ohms")
    
    if Z.imag > 0:
        print(" Diagnóstico: CARGA INDUCTIVA (Ej. Motor)")
    else:
        print(" Diagnóstico: CARGA CAPACITIVA (Ej. Condensador)")

    # ==========================================
    # 5. VISUALIZACIÓN EN PLANO COMPLEJO
    # ==========================================
    plt.figure(figsize=(6, 6))
    # Dibujar el vector desde el origen (0,0) hasta (R, X)
    plt.quiver(0, 0, Z.real, Z.imag, angles='xy', scale_units='xy', scale=1, color='b')
    
    # Configuraciones del gráfico
    plt.xlim(0, Z.real * 1.5)
    plt.ylim(-abs(Z.imag)*1.5, abs(Z.imag)*1.5)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, linestyle='--')
    plt.title("Vector de Impedancia en el Plano Complejo")
    plt.xlabel("Resistencia Real (Ohms)")
    plt.ylabel("Reactancia Imaginaria (Ohms)")
    plt.show()

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
finally:
    esp32.close()
    print("Puerto serial cerrado de forma segura.")