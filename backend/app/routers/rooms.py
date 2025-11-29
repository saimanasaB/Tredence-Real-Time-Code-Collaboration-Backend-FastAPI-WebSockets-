from fastapi import APIRouter
import uuid

router = APIRouter(prefix="/rooms", tags=["Rooms"])

# In-memory room store
rooms = {}

@router.post("")
def create_room():
    room_id = str(uuid.uuid4())[:8]
    rooms[room_id] = {"code": ""}
    return {"roomId": room_id}
