#!/bin/bash

# setup_environment.sh - Environment setup script

set -e  # Exit immediately if a command exits with a non-zero status

# Function to install necessary packages
install_packages() {
    echo "Installing necessary packages..."

    # Update package list and install required packages
    sudo apt update
    sudo apt install -y git curl build-essential

    # Install Node.js and npm
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt install -y nodejs

    # Install Python and pip
    sudo apt install -y python3 python3-pip

    echo "Packages installed successfully!"
}

# Function to set up environment variables
setup_env() {
    echo "Setting up environment variables..."

    # Create a .env file if it doesn't exist
    if [ ! -f .env ]; then
        echo "Creating .env file..."
        touch .env
        echo "DB_HOST=localhost" >> .env
        echo "DB_USER=username" >> .env
        echo "DB_PASS=password" >> .env
        echo "DB_NAME=mydatabase" >> .env
    fi

    echo "Environment variables set up successfully!"
}

# Execute the functions
install_packages
setup_env
