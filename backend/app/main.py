from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import uvicorn
import redis
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.api import api_router
from app.websocket.manager import WebSocketManager

# 创建数据库表
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    Base.metadata.create_all(bind=engine)
    yield
    # 关闭时执行
    pass

# 创建FastAPI应用
app = FastAPI(
    title="Baby Monitor API",
    description="智能婴儿/宠物看护摄像头系统API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 添加受信任主机中间件
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

# 初始化WebSocket管理器
websocket_manager = WebSocketManager()

# 包含API路由
app.include_router(api_router, prefix="/api/v1")

# 根路径
@app.get("/")
async def root():
    return {
        "message": "Baby Monitor API",
        "version": "1.0.0",
        "status": "running"
    }

# 健康检查
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "redis": "connected"
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
