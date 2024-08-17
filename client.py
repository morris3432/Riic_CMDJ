import asyncio
import websockets

async def connect():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from Python")
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

asyncio.run(connect())
