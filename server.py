import asyncio
import websockets
import os

async def handle_connection(websocket, path):
    print("New client connected")
    await websocket.send("Welcome to the Railway WebSocket Test Server (Python)!")
    
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Server received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    port = int(os.getenv("PORT", "3000"))
    server = await websockets.serve(handle_connection, "0.0.0.0", port)
    print(f"Server is listening on port {port}")
    print(f"WebSocket endpoint: ws://localhost:{port}")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
