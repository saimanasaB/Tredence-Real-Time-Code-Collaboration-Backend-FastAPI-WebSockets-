# from fastapi import APIRouter, WebSocket, WebSocketDisconnect

# router = APIRouter()

# rooms_clients = {}    # room_id -> list of websockets
# rooms_code = {}       # room_id -> current code text


# @router.websocket("/ws/{room_id}")
# async def websocket_endpoint(websocket: WebSocket, room_id: str):
#     await websocket.accept()

#     # Create room if not exists
#     rooms_clients.setdefault(room_id, [])
#     rooms_code.setdefault(room_id, "")

#     rooms_clients[room_id].append(websocket)

#     # Send current room code to newly joined client
#     await websocket.send_json({"type": "sync", "code": rooms_code[room_id]})

#     try:
#         while True:
#             data = await websocket.receive_text()

#             # Update room code
#             rooms_code[room_id] = data

#             # Broadcast to all in room except sender
#             for client in rooms_clients[room_id]:
#                 if client is not websocket:
#                     await client.send_json({"type": "update", "code": data})

#     except WebSocketDisconnect:
#         rooms_clients[room_id].remove(websocket)

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.websockets import WebSocketState

router = APIRouter(prefix="/ws")

rooms = {}

@router.websocket("/rooms/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):

    # Accept ALL origins — FIX 403 ERROR
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
