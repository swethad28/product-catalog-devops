from fastapi import APIRouter, HTTPException, Query

router = APIRouter()  

dummy_products = [
    {"id": 1, "name": "Running Shoes", "price": 2999},
    {"id": 2, "name": "Wireless Headphones", "price": 4999},
    {"id": 3, "name": "Laptop Stand", "price": 999}
]

@router.get("/products")
def list_products():
    return {"products": dummy_products}

@router.get("/products/search")
def search_products(
    keyword: str = Query("", description="Keyword to search in product names"),
    min_price: int = Query(0, ge=0, description="Minimum product price"),
    max_price: int = Query(999999, ge=0, description="Maximum product price")
):
    if min_price > max_price:
        raise HTTPException(status_code=400, detail="min_price cannot be greater than max_price")

    filtered_products = [
        product for product in dummy_products
        if keyword.lower() in product["name"].lower()
        and min_price <= product["price"] <= max_price
    ]

    if not filtered_products:
        raise HTTPException(status_code=404, detail="No products found matching the criteria")

    return {"results": filtered_products}
