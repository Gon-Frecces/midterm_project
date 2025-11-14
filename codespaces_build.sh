#!/bin/bash

echo "=== CODESPACES DOCKER DEPLOYMENT ==="

echo "1. Building Docker image..."
docker build -t source-predictor .

echo "2. Stopping any existing containers..."
docker stop source-predictor-app 2>/dev/null || true
docker rm source-predictor-app 2>/dev/null || true

echo "3. Starting new container..."
docker run -d -p 5000:5000 --name source-predictor-app source-predictor

echo "4. Waiting for API to start..."
sleep 8

echo "5. Testing API..."
python codespaces_test.py

echo "=== DEPLOYMENT COMPLETE ==="
echo " Your API is running in Codespaces!"
echo " Open: https://$CODESPACE_NAME-5000.$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN"