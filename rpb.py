import asyncio
import websockets
import RPi.GPIO as GPIO

# Configuración de pines GPIO para el controlador de motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # IN1
GPIO.setup(18, GPIO.OUT)  # IN2
GPIO.setup(22, GPIO.OUT)  # IN3
GPIO.setup(23, GPIO.OUT)  # IN4

async def control_motors(websocket, path):
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        handle_command(message)

def handle_command(command):
    if command == "forward":
        forward()
    elif command == "backward":
        backward()
    elif command == "left":
        left()
    elif command == "right":
        right()
    elif command == "stop":
        stop()
    else:
        print("Comando desconocido")

def forward():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)

def backward():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)

def left():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)

def right():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)

def stop():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)

start_server = websockets.serve(control_motors, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("Servidor WebSocket escuchando en ws://0.0.0.0:8765")
asyncio.get_event_loop().run_forever()