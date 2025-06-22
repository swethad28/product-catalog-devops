from fastapi import FastAPI
from .routes import router as product_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

app.include_router(product_router)
