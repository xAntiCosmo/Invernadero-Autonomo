from machine import Pin, ADC
import network
import urequests
import random
import time
import math

ssid = "INFINITUMB37F_2.4"
password = "L1M3J9V12D1XD"

#Led
led = Pin(2, Pin.OUT)

#Sensor
sensor = ADC(Pin(32))
sensor.atten(ADC.ATTN_11DB) #De 0 a 3.3v
sensor.width(ADC.WIDTH_12BIT)
# Constantes del termistor
BETA = 3950          # Coeficiente Beta
R_NOMINAL = 10000    # Resistencia a 25°C (10k)
T_NOMINAL = 25       # Temperatura de referencia
RESISTENCIA_FIJA = 10000 # La resistencia del divisor

#Wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Conectando a WiFi...")

# Esperar conexión
while not wifi.isconnected():
    time.sleep(0.5)
    print(".", end="")

print("\nConectado!")
print("Configuración de red:", wifi.ifconfig())
    
def enviarDatos():
    url = "https://raw.githubusercontent.com/xAntiCosmo/Invernadero-Autonomo/refs/heads/master/insertData.php"
    
    datos = {
        "temperatura": temperatura,
        }
    headers = {'Content-Type': 'application/json'}
    response = urequests.post(url, json=datos, headers=headers)
    print(response.content)
    
def calcular_celsius(lectura_adc):
    if lectura_adc == 0: return 0 # Evitar división por cero
    
    # 1. Calcular la resistencia del termistor
    # Fórmula para divisor de tensión (Vout = Vin * R2 / (R1 + R2))
    resistencia = RESISTENCIA_FIJA / (4095 / lectura_adc - 1)
    
    # 2. Aplicar ecuación de Steinhart-Hart (simplificada con Beta)
    steinhart = resistencia / R_NOMINAL         # (R/Ro)
    steinhart = math.log(steinhart)             # ln(R/Ro)
    steinhart /= BETA                           # 1/B * ln(R/Ro)
    steinhart += 1.0 / (T_NOMINAL + 273.15)     # + (1/To)
    steinhart = 1.0 / steinhart                 # Invertir
    
    temp_celsius = steinhart - 273.15           # Convertir Kelvin a Celsius
    return round(temp_celsius, 2)

while True:
    led.on()                       # Enciende LED
    lectura_raw = sensor.read()
    temperatura_real = calcular_celsius(lectura_raw)
    print("Temperatura: {}°C".format(temperatura_real))
    
    if wifi.isconnected():
        enviarDatos(temperatura_real)
    
    led.off()
    time.sleep(30)