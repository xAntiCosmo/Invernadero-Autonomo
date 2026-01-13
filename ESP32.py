from machine import Pin, ADC
import network
import urequests
import random
import time

ssid = "INFINITUMB37F_2.4"
password = "L1M3J9V12D1XD"

#Led
led = Pin(2, Pin.OUT)

#Sensor
sensor = ADC(Pin(32))
sensor.atten(ADC.ATTN_11DB) #De 0 a 3.3v
sensor.width(ADC.WIDTH_12BIT)

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

#Leer sensor

print("Presiona para leer")
    
def enviarDatos():
    url = "https://raw.githubusercontent.com/xAntiCosmo/Invernadero-Autonomo/refs/heads/master/insertData.php"
    
    datos = {
        "temperatura": temperatura,
        }
    headers = {'Content-Type': 'application/json'}
    response = urequests.post(url, json=datos, headers=headers)
    print(response.content)

while True:
    led.on()                       # Enciende LED
    temperatura = sensor.read()         # Lee termistor
    print("Temperatura:", temperatura)
    enviarDatos()
    led.off()                      # Apaga LED

    time.sleep(30)                 # Espera 30 segundos