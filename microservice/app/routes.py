from fastapi import APIRouter

router = APIRouter()

dummy_products = [
    {"id": 1, "name": "Running Shoes", "price": 2999},
    {"id": 2, "name": "Wireless Headphones", "price": 4999},
    {"id": 3, "name": "Laptop Stand", "price": 999}
]

@router.get("/products")
def list_products():
    return {"products": dummy_products}
