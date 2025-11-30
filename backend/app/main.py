from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import rooms, autocomplete
from app.websocket_manager import router as ws_router

app = FastAPI(title="Real-time Code Collaboration API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allow WebSocketKing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_websocket_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

app.include_router(rooms.router)
app.include_router(autocomplete.router)
app.include_router(ws_router)
