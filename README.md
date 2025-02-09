Running the Application

This project uses two separate Docker containers:
1. PostgreSQL container (for the database)
2. FastAPI container (for the API)

Step 1: Start PostgreSQL Container
Before running FastAPI, you need to start a PostgreSQL container
Step 2: Start FastAPI Container
docker run --name fastapi-app --network=host -p 8000:8000 fastapi-app  on same network

