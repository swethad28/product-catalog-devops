from fastapi import APIRouter, Query
from typing import List

router = APIRouter()

# Dummy product database
dummy_products = [
    {"id": 1, "name": "Running Shoes", "price": 2999},
    {"id": 2, "name": "Wireless Headphones", "price": 4999},
    {"id": 3, "name": "Laptop Stand", "price": 999}
]

# GET /products - list all products
@router.get("/products")
def list_products():
    return {"products": dummy_products}

# GET /products/search - search products by keyword
@router.get("/products/search")
def search_products(keyword: str = Query("", min_length=1)):
    keyword_lower = keyword.lower()
    results = [product for product in dummy_products if keyword_lower in product["name"].lower()]
    return {"results": results}
