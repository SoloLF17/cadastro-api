from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.person import router

app = FastAPI(docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json")
app.include_router(router)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# REST SOLID API
# GET - PEGAR
# POST - CRIAR
# PUT - ATUALIZAR
# DELETE - MATAR

@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")
