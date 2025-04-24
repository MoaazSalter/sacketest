from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import os
import uvicorn

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome to the Railway WebSocket Test Server (FastAPI)!")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")
            await websocket.send_text(f"Server received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"🔥 Server error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "3000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
