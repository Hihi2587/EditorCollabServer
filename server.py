import asyncio
import os
import websockets

clients = set()

async def handle(websocket):
    clients.add(websocket)
    print("Client connected!")

    try:
        async for message in websocket:
            print(f"Received: {message}")

            disconnected = set()

            for client in clients:
                try:
                    await client.send(message)
                except websockets.exceptions.ConnectionClosed:
                    disconnected.add(client)

            clients.difference_update(disconnected)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

    finally:
        clients.discard(websocket)

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
