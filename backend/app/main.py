from fastapi import FastAPI
from app.api.routes import qa, auth, document, upload
from app.core.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Document Management and RAG-based Q&A App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.on_event("startup")
async def startup():
    await create_db_and_tables()

# Include routes for different functionalities
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(document.router, prefix="/api/documents", tags=["Document Management"])
app.include_router(upload.router, prefix="/api", tags=["Upload Document"])
app.include_router(qa.router, prefix="/api/qa", tags=["Q&A"])

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "API is running"}
