# Use Python image as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from current directory to working directory
COPY . .

# Expose port 8000
EXPOSE 8000

# Start FastAPI server with auto-reload
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
