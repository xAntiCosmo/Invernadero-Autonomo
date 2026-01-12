from machine import Pin, ADC
import network
import urequests
import random
import time

ssid = "INFINITUMB37F_2.4"
password = "L1M3J9V12D1XD"

#Botón
boton = Pin(18, Pin.IN, Pin.PULL_UP)

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
        "TEMPERATURA": valor,
        "ENCENDIDO": random
        }
    headers = {'Content-Type': 'application/json'}
    response = urequests.post(url, json=data, headers=headers)
    print(response.content)

while True:
    if not boton.value():          # Botón presionado
        time.sleep_ms(30)          # Antirrebote
        if not boton.value():

            valor = sensor.read()
            print("Valor ADC:", valor)
            random = random.randint(0,1)
            enviarDatos()

            # Esperar a soltar botón
            while not boton.value():
                pass

    time.sleep_ms(10)