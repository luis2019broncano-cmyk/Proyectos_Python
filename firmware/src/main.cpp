#include <Arduino.h>
// PROGRAMA DE ADQUISICIÓN DE DATOS - ESP32
// ==========================================

// 1. Definición de los pines ADC del ESP32
const int pinVoltaje = 34;   // Conectado a la salida del ZMPT101B
const int pinCorriente = 35; // Conectado a la salida del ACS712

void setup() {
  // 2. Inicializar la comunicación con la computadora (Python)
  // 115200 es la velocidad estándar para enviar datos rápido sin errores
  Serial.begin(115200);

  // 3. Configurar la resolución del Convertidor Analógico a Digital (ADC)
  // El ESP32 tiene un ADC de 12 bits (valores de 0 a 4095)
  analogReadResolution(12); 
  
  // Opcional: Atenuación para que el ESP32 lea hasta 3.3V en el pin
  analogSetPinAttenuation(pinVoltaje, ADC_11db);
  analogSetPinAttenuation(pinCorriente, ADC_11db);
}

void loop() {
  // 4. Leer los valores analógicos de los sensores
  int lecturaVoltaje = analogRead(pinVoltaje);
  int lecturaCorriente = analogRead(pinCorriente);

  // 5. Enviar los datos a la computadora por el cable USB
  // Formato estricto para que Python lo entienda: "Voltaje,Corriente"
  Serial.print(lecturaVoltaje);
  Serial.print(",");
  Serial.println(lecturaCorriente); // println agrega un "Enter" al final

  // 6. Frecuencia de Muestreo (Tiempo entre cada lectura)
  // 1 milisegundo = 1000 muestras por segundo. 
  // Una onda de 60Hz dura 16.6 ms, por lo que tomaremos unas 16 muestras por cada ciclo de la onda.
  delay(1); 
}