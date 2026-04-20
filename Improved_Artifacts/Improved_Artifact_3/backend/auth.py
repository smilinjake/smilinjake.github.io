# Authentication Module for Animal Shelter API
# Handles JWT token validation and user authentication
# Provides dependency injection for protected routes

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

# Secret key for JWT encoding/decoding
SECRET_KEY = "cs499_secret_key"

# OAuth2 scheme for token extraction from requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Dependency function to authenticate and get current user
    Validates JWT token and extracts username from payload
    Raises HTTPException if token is invalid or missing

    Args:
        token (str): JWT access token from Authorization header

    Returns:
        str: Username extracted from token payload

    Raises:
        HTTPException: If token is invalid, expired, or missing username
    """

    try:
        # Decode and validate JWT token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        # Extract username from token payload
        username = payload.get("sub")

        # Check if username exists in payload
        if username is None:
            raise HTTPException(status_code=401)

        return username

    except JWTError:
        # Handle invalid or expired tokens
        raise HTTPException(status_code=401)