FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL files including the model
COPY . .

# Verify the model file is there
RUN ls -la source_model.joblib && echo "✅ Model file verified"

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "predict.py"]gi