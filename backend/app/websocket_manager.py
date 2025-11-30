from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.websockets import WebSocketState

router = APIRouter(prefix="/ws")

rooms = {}

@router.websocket("/rooms/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):

    # Accept ALL origins
    await websocket.accept()

    if room_id not in rooms:
        rooms[room_id] = set()

    rooms[room_id].add(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            
            # Broadcast to all users in the room
            for client in rooms[room_id]:
                if client is not websocket and client.application_state == WebSocketState.CONNECTED:
                    await client.send_text(message)

    except WebSocketDisconnect:
        rooms[room_id].remove(websocket)
