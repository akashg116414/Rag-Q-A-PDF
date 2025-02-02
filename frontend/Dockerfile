# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy frontend files
COPY frontend /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install -r /app/requirements.txt

# Expose port for FastAPI frontend
EXPOSE 8001

# Run the FastAPI frontend server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
