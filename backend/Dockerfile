# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy backend files
COPY backend /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install -r /app/requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
