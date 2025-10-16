#!/usr/bin/env python3
"""
Baby Monitor API 启动脚本
"""
import uvicorn
import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from app.core.config import settings

if __name__ == "__main__":
    # 创建必要的目录
    os.makedirs("logs", exist_ok=True)
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    
    # 启动服务器
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
        access_log=True
    )
