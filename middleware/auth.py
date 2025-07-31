from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import httpx

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("https://auth.internal/validate", json={"token": token})
                if response.status_code != 200:
                    raise HTTPException(status_code=401, detail="Invalid token")
        except httpx.HTTPError:
            raise HTTPException(status_code=503, detail="Auth service unavailable")

        return await call_next(request)