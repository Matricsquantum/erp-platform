from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:3000",  # Local frontend (used in earlier days)
    "http://localhost:3001",  # Local frontend (adjusted to avoid conflicts)
    "https://erp-platform-a.vercel.app",  # Live frontend (as per document)
    "https://erp-platform-4529dk62l-matricsquantums-projects.vercel.app",  # Deployed frontend
    "https://erp-platform-2qfpo5do7-matricsquantums-projects.vercel.app",  # Additional Vercel URL
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

@app.get("/items")
async def get_items():
    return {"items": inventory}

@app.post("/add-item")
async def add_item(item: InventoryItem):
    inventory.append(item.dict())
    return item

@app.get("/orders")
async def get_orders():
    return {"orders": orders}

@app.post("/place-order")
async def place_order(order: OrderItem):
    orders.append(order.dict())
    return order

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Render's PORT or 8000 locally
    uvicorn.run(app, host="0.0.0.0", port=port)