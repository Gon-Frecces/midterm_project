#!/bin/bash

echo "=== Building and Running Source Prediction API ==="

# Build the Docker image
echo "Step 1: Building Docker image..."
docker build -t source-predictor .

# Check if build was successful
if [ $? -eq 0 ]; then
    echo " Docker image built successfully!"
    
    # Stop and remove any existing container with the same name
    echo "Step 2: Cleaning up any existing containers..."
    docker stop source-predictor-app 2>/dev/null || true
    docker rm source-predictor-app 2>/dev/null || true
    
    # Run the container
    echo "Step 3: Starting container..."
    docker run -d \
        -p 5000:5000 \
        --name source-predictor-app \
        source-predictor
    
    echo " Container started successfully!"
    echo ""
    echo "📡 API available at: http://localhost:5000"
    echo "🔍 Check logs with: docker logs source-predictor-app"
    echo "🩺 Check health with: curl http://localhost:5000/health"
    echo "🛑 Stop with: docker stop source-predictor-app"
    echo ""
    echo "⏳ Waiting for container to be ready..."
    sleep 10
    
    # Test the container
    echo "Step 4: Testing container..."
    curl -s http://localhost:5000/health > /dev/null
    
    if [ $? -eq 0 ]; then
        echo "Container is healthy and responding!"
        echo " Deployment successful! Ready for testing."
    else
        echo "  Container started but health check failed. Check logs with: docker logs source-predictor-app"
    fi
else
    echo " Docker build failed!"
    exit 1
fi