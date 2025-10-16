# 婴儿/宠物看护摄像头项目 - 项目概览

## 🎯 项目简介

这是一个基于FastAPI和Android的智能婴儿/宠物看护摄像头系统，集成了AI识别、离线处理、实时监控、双向语音对讲等功能。支持多设备协作，一个手机用于采集视频，另一个手机用于远程查看。

## 📁 项目结构

```
FastApiAndroid/
├── README.md                   # 项目详细说明文档
├── PROJECT_OVERVIEW.md         # 项目概览（本文件）
├── .gitignore                  # Git忽略文件配置
├── upload_to_github.bat        # Windows上传脚本
├── upload_to_github.sh         # Linux/Mac上传脚本
├── backend/                    # FastAPI后端服务
│   ├── app/                    # 应用核心代码
│   │   ├── main.py            # 应用入口
│   │   ├── core/              # 核心配置
│   │   ├── models/            # 数据模型
│   │   ├── schemas/           # 数据模式
│   │   ├── api/               # API接口
│   │   └── websocket/         # WebSocket管理
│   ├── requirements.txt       # Python依赖
│   ├── alembic.ini           # 数据库迁移配置
│   ├── start.py              # 启动脚本
│   └── README.md             # 后端说明文档
└── android/                   # Android应用（待开发）
    ├── app/                   # 应用代码
    ├── build.gradle          # 构建配置
    └── settings.gradle        # 项目设置
```

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/zg919506719/FastApiAndroid.git
cd FastApiAndroid
```

### 2. 启动后端服务
```bash
cd backend
pip install -r requirements.txt
cp env.example .env
# 编辑 .env 文件配置数据库
python start.py
```

### 3. 访问API文档
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## ✨ 核心功能

### 已实现功能
- ✅ 用户认证和授权系统
- ✅ 设备管理和绑定
- ✅ WebSocket实时通信
- ✅ 基础API接口
- ✅ 数据库设计和迁移

### 计划功能
- 🔄 Android应用开发
- 🔄 实时视频流传输
- 🔄 AI智能识别
- 🔄 双向语音对讲
- 🔄 离线数据同步
- 🔄 推送通知系统

## 🛠️ 技术栈

### 后端
- FastAPI + Python 3.8+
- MySQL 8.0+ 数据库
- Redis 缓存
- WebSocket 实时通信
- JWT 认证
- SQLAlchemy ORM

### 前端（计划）
- Android Kotlin + MVVM
- Room 数据库
- WebRTC 音视频通信
- TensorFlow Lite AI推理

## 📊 开发进度

- [x] 项目架构设计
- [x] FastAPI后端开发
- [x] 数据库设计
- [x] API接口设计
- [x] 用户认证系统
- [x] 设备管理系统
- [x] WebSocket通信
- [ ] Android应用开发
- [ ] 视频流处理
- [ ] AI功能集成
- [ ] 语音对讲功能

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📞 联系方式

- 项目链接: [https://github.com/zg919506719/FastApiAndroid](https://github.com/zg919506719/FastApiAndroid)
- 问题反馈: [Issues](https://github.com/zg919506719/FastApiAndroid/issues)

---

**注意**: 这是一个正在开发中的项目，部分功能仍在开发中。欢迎贡献代码和提出建议！
