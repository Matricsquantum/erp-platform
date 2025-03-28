from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://erp-platform-a.vercel.app",
    "https://erp-platform-4529dk62l-matricsquantums-projects.vercel.app",
    "https://erp-platform-2qfpo5do7-matricsquantums-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Pydantic models
class InventoryItem(BaseModel):
    id: int
    name: str
    quantity: int

class OrderItem(BaseModel):
    id: int
    item: str
    quantity: int
    status: str

class LoginRequest(BaseModel):
    username: str
    password: str

# Mock user database (replace with real database later)
users = {"admin": "password"}

# In-memory storage
inventory = [
    {"id": 1, "name": "Item 1", "quantity": 10},
    {"id": 2, "name": "Item 2", "quantity": 5},
]

orders = [
    {"id": 1, "item": "Item 1", "quantity": 5, "status": "Pending"},
]

# Endpoints
@app.get("/")
async def root():
    return {"message": "Hello from ERP Backend"}

@app.post("/login")
async def login(login_request: LoginRequest):
    username = login_request.username
    password = login_request.password
    if username in users and users[username] == password:
        return {"accessToken": "mock-token-123"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/items")
async def get_items(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != "Bearer mock-token-123":
        raise HTTPException(status_code=401, detail="[error_id: 79] accessToken was not sent")
    return {"items": inventory}

@app.post("/add-item")
async def add_item(item: InventoryItem, request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != "Bearer mock-token-123":
        raise HTTPException(status_code=401, detail="[error_id: 79] accessToken was not sent")
    inventory.append(item.dict())
    return item

@app.get("/orders")
async def get_orders(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != "Bearer mock-token-123":
        raise HTTPException(status_code=401, detail="[error_id: 79] accessToken was not sent")
    return {"orders": orders}

@app.post("/place-order")
async def place_order(order: OrderItem, request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != "Bearer mock-token-123":
        raise HTTPException(status_code=401, detail="[error_id: 79] accessToken was not sent")
    orders.append(order.dict())
    return order

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
