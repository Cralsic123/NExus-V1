from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

# room_name -> active connections
rooms = {}

@router.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):

    await websocket.accept()

    if room not in rooms:
        rooms[room] = []

    rooms[room].append(websocket)

    try:
        while True:
            message = await websocket.receive_text()

            # broadcast to everyone in room
            for client in rooms[room]:
                await client.send_text(message)

    except WebSocketDisconnect:
        rooms[room].remove(websocket)