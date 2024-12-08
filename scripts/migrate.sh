#!/bin/bash

# migrate.sh - Database migration script

set -e  # Exit immediately if a command exits with a non-zero status

# Load environment variables
source .env

# Define database connection variables
DB_HOST="localhost"
DB_USER="username"
DB_PASS="password"
DB_NAME="mydatabase"

# Function to run migrations
migrate() {
    echo "Starting database migration..."

    # Run database migrations
    npx sequelize-cli db:migrate  # For Node.js with Sequelize
    # or for Python with Alembic
    # alembic upgrade head

    echo "Database migration completed successfully!"
}

# Execute the migrate function
migrate
