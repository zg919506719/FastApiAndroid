# Docker 部署指南

## 🐳 项目Docker化部署

本项目支持使用Docker和Docker Compose进行容器化部署，包含完整的后端服务、数据库、缓存和反向代理。

## 📁 Docker文件结构

```
FastApiAndroid/
├── docker-compose.yml          # 开发环境配置
├── docker-compose.prod.yml     # 生产环境配置
├── env.docker                  # Docker环境变量
├── nginx/                      # Nginx配置
│   ├── nginx.conf
│   └── conf.d/default.conf
└── backend/
    ├── Dockerfile              # 后端服务镜像
    └── requirements.txt
```

## 🚀 快速开始

### 1. 环境准备

确保已安装以下软件：
- Docker 20.10+
- Docker Compose 2.0+

### 2. 克隆项目

```bash
git clone https://github.com/zg919506719/FastApiAndroid.git
cd FastApiAndroid
```

### 3. 配置环境变量

```bash
# 复制环境配置文件
cp env.docker .env

# 编辑环境变量
nano .env
```

重要配置项：
```env
# 数据库配置
MYSQL_ROOT_PASSWORD=your_secure_password_here
MYSQL_DATABASE=baby_monitor
MYSQL_USER=baby_monitor
MYSQL_PASSWORD=your_secure_password_here

# 应用配置
SECRET_KEY=your-super-secret-key-change-in-production
DEBUG=False
```

### 4. 启动服务

#### 开发环境
```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f backend
```

#### 生产环境
```bash
# 使用生产环境配置
docker-compose -f docker-compose.prod.yml up -d
```

### 5. 访问服务

- **API文档**: http://localhost:8000/docs
- **应用接口**: http://localhost:8000/api/v1/
- **健康检查**: http://localhost:8000/health

## 🔧 服务配置

### 服务列表

| 服务 | 端口 | 描述 |
|------|------|------|
| backend | 8000 | FastAPI后端服务 |
| mysql | 3306 | MySQL数据库 |
| redis | 6379 | Redis缓存 |
| nginx | 80/443 | 反向代理 |

### 数据库初始化

数据库会在首次启动时自动创建，包含以下表：
- users (用户表)
- devices (设备表)
- user_devices (用户设备关联表)
- connection_logs (连接日志表)
- offline_data (离线数据表)

### 数据持久化

数据通过Docker volumes持久化：
- `mysql_data`: MySQL数据
- `redis_data`: Redis数据
- `./backend/uploads`: 上传文件
- `./backend/logs`: 日志文件

## 🛠️ 开发指南

### 本地开发

1. **启动后端服务**:
```bash
cd backend
docker-compose up -d mysql redis
python start.py
```

2. **Android应用开发**:
```bash
cd android
# 使用Android Studio打开项目
```

### 代码热重载

开发环境下，后端代码修改会自动重载：
```bash
# 启动开发环境
docker-compose up -d

# 查看实时日志
docker-compose logs -f backend
```

### 数据库管理

```bash
# 连接MySQL
docker-compose exec mysql mysql -u root -p

# 备份数据库
docker-compose exec mysql mysqldump -u root -p baby_monitor > backup.sql

# 恢复数据库
docker-compose exec -T mysql mysql -u root -p baby_monitor < backup.sql
```

## 🔒 安全配置

### 生产环境安全

1. **修改默认密码**:
```env
MYSQL_ROOT_PASSWORD=your_very_secure_password
MYSQL_PASSWORD=your_very_secure_password
SECRET_KEY=your_very_long_and_secure_secret_key
```

2. **启用HTTPS**:
```bash
# 将SSL证书放在nginx/ssl/目录
# 修改nginx配置启用HTTPS
```

3. **防火墙配置**:
```bash
# 只开放必要端口
ufw allow 80
ufw allow 443
ufw deny 3306  # 不对外暴露数据库端口
ufw deny 6379  # 不对外暴露Redis端口
```

### 环境变量安全

生产环境建议使用环境变量文件：
```bash
# 创建生产环境变量文件
cp env.docker .env.prod

# 使用生产环境变量
docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d
```

## 📊 监控和日志

### 日志查看

```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs backend
docker-compose logs mysql
docker-compose logs redis

# 实时查看日志
docker-compose logs -f backend
```

### 服务监控

```bash
# 查看服务状态
docker-compose ps

# 查看资源使用情况
docker stats

# 重启服务
docker-compose restart backend
```

### 健康检查

```bash
# 检查API健康状态
curl http://localhost:8000/health

# 检查数据库连接
docker-compose exec backend python -c "from app.core.database import engine; print(engine.execute('SELECT 1').scalar())"
```

## 🔄 更新和部署

### 更新应用

```bash
# 拉取最新代码
git pull

# 重新构建镜像
docker-compose build backend

# 重启服务
docker-compose up -d backend
```

### 数据库迁移

```bash
# 进入后端容器
docker-compose exec backend bash

# 运行数据库迁移
alembic upgrade head
```

### 备份和恢复

```bash
# 备份数据
docker-compose exec mysql mysqldump -u root -p baby_monitor > backup_$(date +%Y%m%d_%H%M%S).sql

# 恢复数据
docker-compose exec -T mysql mysql -u root -p baby_monitor < backup_file.sql
```

## 🐛 故障排除

### 常见问题

1. **端口冲突**:
```bash
# 检查端口占用
netstat -tulpn | grep :8000

# 修改端口配置
# 编辑docker-compose.yml中的端口映射
```

2. **数据库连接失败**:
```bash
# 检查数据库状态
docker-compose logs mysql

# 重启数据库
docker-compose restart mysql
```

3. **权限问题**:
```bash
# 修复文件权限
sudo chown -R $USER:$USER ./backend/uploads
sudo chown -R $USER:$USER ./backend/logs
```

### 日志分析

```bash
# 查看错误日志
docker-compose logs backend | grep ERROR

# 查看访问日志
docker-compose logs nginx | grep "GET\|POST"
```

## 📈 性能优化

### 资源限制

```yaml
# docker-compose.yml
services:
  backend:
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
```

### 数据库优化

```yaml
# MySQL配置优化
mysql:
  command: >
    --default-authentication-plugin=mysql_native_password
    --innodb-buffer-pool-size=256M
    --max-connections=100
```

## 🔗 相关链接

- [Docker官方文档](https://docs.docker.com/)
- [Docker Compose文档](https://docs.docker.com/compose/)
- [FastAPI部署指南](https://fastapi.tiangolo.com/deployment/)
- [MySQL Docker镜像](https://hub.docker.com/_/mysql)
- [Redis Docker镜像](https://hub.docker.com/_/redis)
