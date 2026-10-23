from fastapi import FastAPI
from app.api.person import router

app = FastAPI(docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json")
app.include_router(router)

# REST SOLID API
# GET - PEGAR
# POST - CRIAR
# PUT - ATUALIZAR
# DELETE - MATAR

@app.get("/")
def home():
    return {
        "message": "Hello World"
    }
