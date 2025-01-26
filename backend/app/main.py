from fastapi import FastAPI
from app.api.routes import ingestion, qa, auth, document
from app.core.database import create_db_and_tables

app = FastAPI(title="Document Management and RAG-based Q&A App")

@app.on_event("startup")
async def startup():
    await create_db_and_tables()

# Include routes for different functionalities
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(document.router, prefix="/api/documents", tags=["Document Management"])
app.include_router(ingestion.router, prefix="/api/ingestion", tags=["Ingestion"])
app.include_router(qa.router, prefix="/api/qa", tags=["Q&A"])

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "API is running"}
