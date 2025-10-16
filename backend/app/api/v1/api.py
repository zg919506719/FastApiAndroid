from fastapi import APIRouter
from app.api.v1.endpoints import auth, devices, websocket

api_router = APIRouter()

# 包含各个端点路由
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(devices.router, prefix="/devices", tags=["设备管理"])
api_router.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])
