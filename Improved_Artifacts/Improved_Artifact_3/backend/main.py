# Animal Shelter API - Main FastAPI Application
# Provides REST endpoints for CRUD operations on animal shelter data
# Includes authentication and CORS middleware for frontend integration

from fastapi import FastAPI, Depends, HTTPException
from jose import jwt
from CRUD_Python_Module import AnimalShelter
from auth import get_current_user, SECRET_KEY
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI application
app = FastAPI()

# Configure CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database connection
db = AnimalShelter("aacuser", "admin")


@app.get("/")
def root():
    """
    Root endpoint - Health check for API
    Returns status message indicating API is running
    """
    return {"message": "Animal Shelter API running"}


@app.post("/login")
def login(username: str, password: str):
    """
    Authentication endpoint - Generates JWT access token
    Validates hardcoded credentials and returns JWT token

    Args:
        username (str): User login name
        password (str): User password

    Returns:
        dict: Access token for authenticated requests

    Raises:
        HTTPException: If credentials are invalid
    """

    # Check credentials (hardcoded for demo)
    if username == "admin" and password == "password":

        # Generate JWT token with username payload
        token = jwt.encode(
            {"sub": username},
            SECRET_KEY,
            algorithm="HS256"
        )

        return {"access_token": token}

    # Raise exception for invalid credentials
    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )


@app.get("/animals")
def get_animals(current_user: str = Depends(get_current_user)):
    """
    GET /animals - Retrieve all animal records
    Requires authentication via JWT token

    Returns:
        list: Array of animal objects with converted _id strings
    """

    # Fetch all animal records from database
    animals = list(db.read({}))

    # Convert ObjectId to string for JSON serialization
    for animal in animals:
        animal["_id"] = str(animal["_id"])

    return animals


@app.post("/animals")
def create_animal(data: dict,
                  user=Depends(get_current_user)):
    """
    POST /animals - Create new animal record
    Requires authentication and valid animal data

    Args:
        data (dict): Animal data to create
        user: Authenticated user (dependency injection)

    Returns:
        dict: Created animal document
    """
    return db.create(data)


@app.put("/animals")
def update_animal(query: dict,
                  data: dict,
                  user=Depends(get_current_user)):
    """
    PUT /animals - Update existing animal record
    Requires authentication and valid query/data

    Args:
        query (dict): MongoDB query to find record
        data (dict): Updated animal data
        user: Authenticated user (dependency injection)

    Returns:
        dict: Update operation result
    """
    return db.update(query, data)


@app.delete("/animals")
def delete_animal(query: dict,
                  user=Depends(get_current_user)):
    """
    DELETE /animals - Remove animal record
    Requires authentication and valid query

    Args:
        query (dict): MongoDB query to find record for deletion
        user: Authenticated user (dependency injection)

    Returns:
        dict: Delete operation result
    """
    return db.delete(query)