from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image: str
    category: str

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    items: List[OrderItem]
    total_amount: int
    customer_name: str
    address: str
    phone: str

# Mock Database
products = [
    {
        "id": 1,
        "name": "Classic Banana Chips",
        "description": "Authentic Kerala style fried banana chips made in coconut oil.",
        "price": 120,
        "image": "/images/banana-chips.jpg",
        "category": "Chips"
    },
    {
        "id": 2,
        "name": "Spicy Masala Wafers",
        "description": "Crispy potato wafers tossed in a special Maharashtrian spice mix.",
        "price": 80,
        "image": "/images/wafers.jpg",
        "category": "Wafers"
    },
    {
        "id": 3,
        "name": "Yellow Banana Wafers",
        "description": "Thinly sliced yellow banana wafers, salted to perfection.",
        "price": 130,
        "image": "/images/yellow-banana-chips.jpg",
        "category": "Chips"
    },
    {
        "id": 4,
        "name": "Tomato Wafers",
        "description": "Tangy tomato flavored potato wafers.",
        "price": 90,
        "image": "/images/tomato-wafers.jpg",
        "category": "Wafers"
    },
    {
        "id": 5,
        "name": "Pepper Banana Chips",
        "description": "Spicy pepper flavored banana chips.",
        "price": 125,
        "image": "/images/banana-chips.jpg",
        "category": "Chips"
    },
    {
        "id": 6,
        "name": "Tapioca Chips",
        "description": "Crunchy tapioca chips, a Kerala specialty.",
        "price": 110,
        "image": "/images/yellow-banana-chips.jpg",
        "category": "Chips"
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to Maharashtrian Snacks API"}

@app.get("/products", response_model=List[Product])
def get_products():
    return products

@app.post("/order")
def place_order(order: Order):
    print(f"Order received from {order.customer_name}:")
    print(f"Address: {order.address}, Phone: {order.phone}")
    print(f"Items: {order.items}")
    print(f"Total: {order.total_amount}")
    return {"message": f"Order placed successfully for {order.customer_name}!", "order_id": 12345}
