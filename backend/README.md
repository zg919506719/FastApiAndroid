# Baby Monitor API 后端服务

## 项目概述

这是婴儿/宠物看护摄像头系统的后端API服务，基于FastAPI框架开发，提供用户认证、设备管理、WebSocket实时通信等功能。

## 技术栈

- **FastAPI**: 现代化的Python Web框架
- **SQLAlchemy**: ORM数据库操作
- **MySQL**: 主数据库
- **Redis**: 缓存和会话管理
- **WebSocket**: 实时通信
- **JWT**: 用户认证
- **Alembic**: 数据库迁移

## 功能特性

### 已实现功能
- ✅ 用户注册和登录
- ✅ JWT令牌认证
- ✅ 设备管理（注册、绑定、解绑）
- ✅ WebSocket实时通信
- ✅ 基础API接口

### 待实现功能
- 🔄 视频流处理
- 🔄 AI模型集成
- 🔄 文件上传管理
- 🔄 推送通知
- 🔄 健康数据管理

## 安装和运行

### 环境要求

- Python 3.8+
- MySQL 8.0+
- Redis 6.0+

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置环境

1. 复制环境配置文件：
```bash
cp env.example .env
```

2. 编辑 `.env` 文件，配置数据库和Redis连接信息：
```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/baby_monitor
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key-here
```

### 数据库初始化

1. 创建数据库：
```sql
CREATE DATABASE baby_monitor CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. 运行数据库迁移：
```bash
alembic upgrade head
```

### 启动服务

```bash
python start.py
```

或者使用uvicorn直接启动：
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API文档

启动服务后，访问以下地址查看API文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 主要API端点

### 用户认证
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/login` - 用户登录
- `POST /api/v1/auth/refresh` - 刷新令牌
- `POST /api/v1/auth/logout` - 用户登出
- `GET /api/v1/auth/profile` - 获取用户信息

### 设备管理
- `GET /api/v1/devices/` - 获取设备列表
- `POST /api/v1/devices/` - 注册新设备
- `GET /api/v1/devices/{device_id}` - 获取设备详情
- `PUT /api/v1/devices/{device_id}` - 更新设备信息
- `DELETE /api/v1/devices/{device_id}` - 删除设备
- `POST /api/v1/devices/{device_id}/bind` - 绑定设备
- `POST /api/v1/devices/{device_id}/unbind` - 解绑设备

### WebSocket
- `WS /api/v1/ws/camera/{device_id}` - 摄像头连接
- `WS /api/v1/ws/viewer/{device_id}` - 查看端连接

## 项目结构

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # 应用入口
│   ├── core/
│   │   ├── config.py          # 配置管理
│   │   ├── database.py        # 数据库连接
│   │   └── security.py        # 安全相关
│   ├── models/
│   │   ├── user.py            # 用户模型
│   │   ├── device.py          # 设备模型
│   │   └── user_device.py     # 用户设备关联模型
│   ├── schemas/
│   │   ├── auth.py            # 认证相关模式
│   │   └── device.py          # 设备相关模式
│   ├── api/
│   │   └── v1/
│   │       ├── api.py         # API路由汇总
│   │       └── endpoints/
│   │           ├── auth.py    # 认证端点
│   │           ├── devices.py # 设备管理端点
│   │           └── websocket.py # WebSocket端点
│   └── websocket/
│       └── manager.py         # WebSocket管理器
├── alembic/                   # 数据库迁移
├── requirements.txt           # 依赖包
├── alembic.ini               # Alembic配置
├── start.py                  # 启动脚本
└── README.md                 # 项目说明
```

## 开发说明

### 数据库迁移

创建新的迁移文件：
```bash
alembic revision --autogenerate -m "描述信息"
```

应用迁移：
```bash
alembic upgrade head
```

回滚迁移：
```bash
alembic downgrade -1
```

### 代码规范

- 使用Black进行代码格式化
- 使用isort进行导入排序
- 遵循PEP 8编码规范

### 测试

运行测试：
```bash
pytest
```

## 部署

### Docker部署

```bash
docker build -t baby-monitor-api .
docker run -p 8000:8000 baby-monitor-api
```

### 生产环境配置

1. 设置环境变量
2. 配置反向代理（Nginx）
3. 启用HTTPS
4. 配置监控和日志

## 许可证

MIT License
