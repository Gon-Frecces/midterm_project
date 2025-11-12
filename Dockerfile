FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL files (including model)
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "predict.py"]