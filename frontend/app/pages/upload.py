from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import httpx

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/upload")
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    async with httpx.AsyncClient(follow_redirects=False) as client:
        files = {"file": (file.filename, file.file, file.content_type)}
        response = await client.post("http://localhost:8000/api/upload/", files=files)
        
        if response.status_code == 200:
            return response.json()
        return JSONResponse(content={"detail": "Upload failed"}, status_code=400)
