#!/bin/bash

# deploy.sh - Deployment script for the application

set -e  # Exit immediately if a command exits with a non-zero status

# Load environment variables
source .env

# Define variables
APP_DIR="/var/www/myapp"
REPO_URL="https://github.com/username/myapp.git"
BRANCH="main"

# Function to deploy the application
deploy() {
    echo "Starting deployment..."

    # Pull the latest code
    if [ -d "$APP_DIR" ]; then
        cd "$APP_DIR"
        git checkout "$BRANCH"
        git pull origin "$BRANCH"
    else
        git clone "$REPO_URL" "$APP_DIR"
        cd "$APP_DIR"
    fi

    # Install dependencies
    echo "Installing dependencies..."
    npm install  # or pip install -r requirements.txt for Python apps

    # Build the application
    echo "Building the application..."
    npm run build  # or any other build command

    # Restart the application service
    echo "Restarting application service..."
    systemctl restart myapp.service

    echo "Deployment completed successfully!"
}

# Execute the deploy function
deploy
