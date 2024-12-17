#!/bin/bash

# migrate.sh

# Check if the migration tool is installed
if ! command -v alembic &> /dev/null
then
    echo "Alembic could not be found. Please install it to proceed."
    exit 1
fi

# Run migrations
echo "Running database migrations..."
alembic upgrade head

if [ $? -eq 0 ]; then
    echo "Migrations completed successfully."
else
    echo "Migrations failed. Please check the error messages above."
    exit 1
fi
