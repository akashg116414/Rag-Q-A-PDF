# Document Management and RAG-based Q&A Application

This is a **Full-Stack FastAPI application** that includes:  
✅ A **Backend API** built with FastAPI & SQLite  
✅ A **Frontend UI** using FastAPI & Jinja Templates  
✅ **Document Upload & Q&A System** using FAISS for Retrieval-Augmented Generation (RAG)  
✅ **Dockerized Setup** for easy deployment  

---

## 📌 1️⃣ Prerequisites  
Before running the project, make sure you have:  
✅ **Python 3.10+** installed  
✅ **Docker & Docker Compose** installed ([Download Here](https://www.docker.com/get-started))  

---

## 📌 2️⃣ Running the Project Locally  

### 🔹 **Step 1: Clone the Repository**  
```sh
git clone https://github.com/akashg116414/Rag-Q-A-PDF.git
cd Rag-Q-A-PDF
```

### 🔹 **Step 2: Create & Activate a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 🔹 **Step 3: Install Dependencies**  
```sh
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 🔹 **Step 4: Setup `.env` File for API Key**  
You must create a `.env` file in the `backend/` folder and add your OpenAI API key:  
```sh
cd backend
touch .env  # macOS/Linux
echo OPENAI_API_KEY=your-api-key-here > .env  # Windows PowerShell
```
📌 **Edit `backend/.env` and add your API Key:**  
```sh
OPENAI_API_KEY=your-api-key-here
```

### 🔹 **Step 5: Run Backend API**
```sh
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
✅ **API Running at**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🔹 **Step 6: Run Frontend**
Open a new terminal window and run:
```sh
cd frontend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```
✅ **Frontend Running at**: [http://localhost:8001](http://localhost:8001)

---

## 📌 3️⃣ Running with Docker Compose  
Instead of running manually, you can use **Docker Compose** to start both services.

### 🔹 **Step 1: Build and Start Containers**  
```sh
docker-compose up --build
```

### 🔹 **Step 2: Check Running Services**
Once the containers are running, you can check:  
✅ **Backend API** → [http://localhost:8000/docs](http://localhost:8000/docs)  
✅ **Frontend UI** → [http://localhost:8001](http://localhost:8001)  

### 🔹 **Step 3: Stop Containers**
To stop all running services:  
```sh
docker-compose down
```

---

## 📌 4️⃣ API Endpoints

### 🔹 **Backend Endpoints (`http://localhost:8000`)**  

| Endpoint                 | Method | Description                 |
|--------------------------|--------|-----------------------------|
| `/api/upload`            | POST   | Upload a PDF document       |
| `/api/documents/list`    | GET    | List uploaded PDFs          |
| `/api/qa/ask`            | POST   | Ask a question from a PDF   |

---

## 📌 5️⃣ Project Structure  
```
fastapi-qa-app/
│── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── upload.py  # Handles PDF uploads
│   │   │   │   ├── qa.py  # Handles Q&A processing
│   │   │   ├── main.py  # FastAPI app entry point
│   │   ├── core/
│   │   │   ├── config.py  # API key & database settings
│   │   ├── models/
│   │   │   ├── document.py  # Document metadata model
│   │   ├── utils/
│   │   │   ├── pdf_utils.py  # Extracts text from PDFs
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
│
│── frontend/
│   ├── app/
│   │   ├── main.py  # FastAPI app entry point
│   │   ├── templates/
│   │   │   ├── upload.html  # Upload page UI
│   │   │   ├── qa.html  # Q&A page UI
│   ├── requirements.txt
│   ├── Dockerfile
│
│── docker-compose.yml  # Manages backend & frontend containers
│── README.md
```

---

## 📌 6️⃣ Notes & Troubleshooting  

### 🔹 **Common Issues**
1️⃣ **Port Already in Use?**  
- Make sure **ports 8000 & 8001** are free. If another app is using them, stop it first:
  ```sh
  lsof -i :8000  # Find process using port 8000 (Linux/macOS)
  kill -9 <PID>  # Replace <PID> with actual process ID
  ```

2️⃣ **.env Not Loaded?**  
- Ensure the `.env` file is inside the `backend/` folder and contains:
  ```sh
  OPENAI_API_KEY=your-api-key-here
  ```

3️⃣ **Container Won't Start?**  
- If Docker services fail, try **rebuilding them**:
  ```sh
  docker-compose down --volumes  # Remove old containers
  docker-compose up --build
  ```

---
📌 **Author:** Akash Garg
📌 **GitHub Repo:** [https://github.com/akashg116414](https://github.com/akashg116414)

