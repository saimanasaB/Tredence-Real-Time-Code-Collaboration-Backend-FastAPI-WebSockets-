This project is a lightweight backend service that supports real-time collaborative code editing between two users. It is built using FastAPI, WebSockets, and Python, and focuses on simplicity, performance, and clarity.

Key Features:

1. Real-Time Collaboration
Multiple users can join the same room. Live code updates are broadcast instantly to all connected clients. Each room maintains its own latest code state.

2. Room Management
Create new rooms with a unique ID. Join existing rooms through a simple REST API.

3. WebSocket-Based Sync
Bi-directional communication between server and connected clients. Handles connection join/leave, broadcast updates, and active users.

4. Autocomplete API
Basic autocomplete suggestions for common Python keywords. Useful for integrating with an editor frontend.

5. Clean Project Structure
Routers organized by feature. WebSocket manager separated for easy maintenance.

Requirements file included.

Project Structure:
backend/
│── app/
│   │── main.py
│   │── websocket_manager.py
│   └── routers/
│        │── rooms.py
│        └── autocomplete.py
│
├── requirements.txt
└── .gitignore


API Endpoints
1. Create Room
GET /rooms/create
Returns a new room ID.

2. Join Room
GET /rooms/join?id=<room_id>
Validates and joins a room.

3. Autocomplete
GET /autocomplete?query=<text>

WebSocket Endpoint
Connect to Room
ws://localhost:8000/ws/<room_id>

Events Supported

join → User enters the room

sync_code → Update and broadcast current editor text

leave → On disconnect

How to Run:
Install dependencies
pip install -r requirements.txt

Start the server:
uvicorn backend.app.main:app --reload

Server runs on: http://localhost:8000

Notes:
This is a backend-only prototype (no database, no authentication).
Intended for evaluation purposes and easy integration with any frontend editor.
Focus is on clarity and demonstrating real-time WebSocket handling.

## Future Enhancements
- Add user presence indicators (who is currently typing)
- Add persistence layer to store room history
- Add authentication for private rooms

License: This project is created for technical evaluation purposes.
