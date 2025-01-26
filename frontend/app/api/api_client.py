import httpx

API_BASE_URL = "http://localhost:8000/api"

async def fetch_dashboard_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/documents")
        return response.json()

async def post_question(question: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/qa", json={"question": question})
        return response.json()

async def upload_document(title: str, content: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/documents", json={"title": title, "content": content})
        return response.json()
