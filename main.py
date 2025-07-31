from fastapi import FastAPI
from middleware.auth import AuthMiddleware
from routers import ai, blockchain, analyzer, user, swiftbot

app = FastAPI()

# Apply shared token validation
app.add_middleware(AuthMiddleware)

# Register routers
app.include_router(ai.router, prefix="/ai")
app.include_router(blockchain.router, prefix="/blockchain")
app.include_router(analyzer.router, prefix="/analyzer")
app.include_router(user.router, prefix="/user")
app.include_router(swiftbot.router, prefix="/swiftbot")