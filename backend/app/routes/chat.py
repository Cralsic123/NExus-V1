from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

router = APIRouter()

rooms = {}

@router.websocket("/ws/{room}")
async def websocket_endpoint(
    websocket: WebSocket,
    room: str
):

    await websocket.accept()

    if room not in rooms:
        rooms[room] = []

    rooms[room].append(websocket)

    try:

        while True:

            data = await websocket.receive_text()

            for client in rooms[room]:

                await client.send_text(data)

    except WebSocketDisconnect:

        rooms[room].remove(websocket)