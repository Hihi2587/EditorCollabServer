import asyncio
import os
import websockets

async def handle(websocket):
    print("Client connected!")

    try:
        async for message in websocket:
            print(f"Received: {message}")

            await websocket.send(
                f"Server received: {message}"
            )

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

async def main():
    port = int(os.environ.get("PORT", 8080))

    print(f"Starting server on port {port}")

    async with websockets.serve(
        handle,
        "0.0.0.0",
        port
    ):
        print("Server is running!")
        await asyncio.Future()

asyncio.run(main())