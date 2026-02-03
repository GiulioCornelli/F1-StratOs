from fastapi import APIRouter, HTTPException, status
import httpx
from ..models.auth import UserRegister, UserLogin, LoginResponse

routerAuth = APIRouter(prefix="/api/auth", tags=["Authentication"])

AUTH_SERVICE_URL = "http://127.0.0.1:8000"

@routerAuth.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{AUTH_SERVICE_URL}/register", json=user_data.model_dump())
            
        if response.status_code != 201:
            try:
                error_detail = response.json().get("detail", "Registration failed")
            except Exception:
                error_detail = f"Auth Service Error ({response.status_code})"
            raise HTTPException(status_code=response.status_code, detail=error_detail)
            
        return response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Auth service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Gateway Error: {str(e)}")

@routerAuth.post("/login", response_model=LoginResponse)
async def login(credentials: UserLogin):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{AUTH_SERVICE_URL}/login", json=credentials.model_dump())
            
        if response.status_code != 200:
            try:
                error_detail = response.json().get("detail", "Login failed")
            except Exception:
                error_detail = f"Auth Service Error ({response.status_code})"
            raise HTTPException(status_code=response.status_code, detail=error_detail)
            
        return response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Auth service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Gateway Error: {str(e)}")
