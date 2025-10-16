# 婴儿/宠物看护摄像头项目

## 项目概述

这是一个基于FastAPI和Android的智能婴儿/宠物看护摄像头系统，集成了AI识别、离线处理、实时监控等功能。支持多设备协作，一个手机用于采集视频，另一个手机用于远程查看，并具备智能分析和离线数据同步能力。

## 技术栈

### 后端
- **FastAPI**: 现代化的Python Web框架
- **WebSocket**: 实时视频流传输
- **OpenCV**: 视频处理和图像分析
- **MySQL**: 数据存储
- **JWT**: 用户认证和授权
- **TensorFlow**: AI模型服务端推理
- **Redis**: 缓存和会话管理
- **FFmpeg**: 视频编码和转码
- **WebRTC**: 实时音视频通信
- **Opus**: 音频编码

### 前端
- **Android**: Kotlin + MVVM架构
- **传统View系统**: 不使用Compose
- **Retrofit**: 网络请求
- **LiveData**: 数据绑定
- **Camera2 API**: 摄像头控制
- **Room**: 本地数据库
- **WorkManager**: 后台任务处理
- **TensorFlow Lite**: 移动端AI推理
- **DataStore**: 设置存储
- **ExoPlayer**: 视频播放
- **Firebase**: 推送通知和崩溃报告
- **Google Maps**: 位置服务
- **Biometric**: 生物识别认证
- **WebRTC**: 实时音视频通信
- **AudioRecord/AudioTrack**: 音频录制和播放

## 项目结构

```
FastApiAndroid/
├── backend/                 # FastAPI后端
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # 主应用入口
│   │   ├── models/         # 数据模型
│   │   ├── routers/        # API路由
│   │   ├── services/       # 业务逻辑
│   │   └── utils/          # 工具函数
│   ├── requirements.txt
│   └── README.md
├── android/                # Android应用
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── java/com/babymonitor/
│   │   │   │   ├── ui/     # UI层
│   │   │   │   ├── viewmodel/ # ViewModel层
│   │   │   │   ├── repository/ # Repository层
│   │   │   │   ├── network/ # 网络层
│   │   │   │   ├── camera/  # 摄像头相关
│   │   │   │   └── utils/   # 工具类
│   │   │   ├── res/        # 资源文件
│   │   │   └── AndroidManifest.xml
│   │   └── build.gradle
│   └── build.gradle
└── README.md
```

## 功能特性

### 采集端功能
- 📹 实时视频采集和编码
- 🔄 自动重连机制
- 📱 前后摄像头切换
- ⚙️ 视频质量调节（720p/1080p/4K）
- 🔒 设备认证和绑定
- 🤖 本地AI识别（哭声检测、异常行为）
- 📱 离线视频录制和缓存
- 🔔 智能推送通知
- 📊 实时状态监控

### 查看端功能
- 👀 实时视频查看
- 📱 多设备支持
- 🔄 自动重连
- 📊 连接状态显示
- ⚙️ 视频质量选择
- 📱 远程设备控制
- 🔔 实时通知接收
- 📈 历史数据查看
- 🎛️ 远程设置调整
- 🎤 双向语音对讲（与家人/宠物实时通话）

### 后端功能
- 🌐 RESTful API
- 🔌 WebSocket实时通信
- 🔐 JWT用户认证和授权
- 📊 设备管理和绑定
- 📈 连接状态监控
- 🤖 AI模型服务（云端推理）
- 📱 推送通知服务
- 💾 视频存储和管理
- 📊 数据分析和统计
- 🔄 离线数据同步
- 🎤 语音对讲服务（音频流处理）

### AI智能识别功能
- 👶 婴儿哭声检测
- 🐕 宠物异常行为识别
- 👤 人脸识别和追踪
- 🚨 异常事件检测
- 📊 行为模式分析
- 🔔 智能预警系统
- 🌡️ 体温异常检测（红外摄像头）
- 💤 睡眠质量监测
- 🍼 喂养提醒和记录
- 🏃 活动量统计

### 高级功能
- 📱 多用户家庭管理
- 👥 家庭成员权限控制
- 📅 日程安排和提醒
- 📊 健康数据统计
- 🎵 白噪音播放
- 🌙 夜视模式
- 🎤 双向语音对讲（实时通话）
  - 高清语音通话
  - 低延迟音频传输
  - 噪音抑制和回声消除
  - 音量调节和静音控制
  - 一键通话功能
- 🔒 隐私保护模式
- 📱 多平台支持（iOS/Web）
- 🌐 云端备份和恢复
- 🔐 端到端加密
- 🛡️ 隐私保护
- 📱 生物识别登录
- 🌍 多语言支持
- 📊 数据分析和报告
- 🎯 个性化推荐
- 🔔 智能通知管理
- 📱 小部件支持
- 🌙 深色模式

## 应用架构

### Android MVVM架构
```
UI Layer (Activity/Fragment)
    ↓
ViewModel (处理UI逻辑)
    ↓
Repository (数据仓库)
    ↓
Local Database (Room) ← → Network Service (Retrofit)
    ↓                           ↓
Offline Sync (WorkManager)   FastAPI Backend
    ↓                           ↓
AI Processing (TensorFlow Lite)  AI Service (TensorFlow)
```

### 主要组件

#### UI层
- **MainActivity**: 主入口，用户登录和模式选择
- **LoginActivity**: 用户登录界面
- **CameraActivity**: 摄像头采集界面
- **ViewerActivity**: 视频查看界面
- **SettingsActivity**: 设置界面
- **DeviceManagementActivity**: 设备管理界面

#### ViewModel层
- **AuthViewModel**: 用户认证逻辑
- **CameraViewModel**: 摄像头控制逻辑
- **ViewerViewModel**: 视频查看逻辑
- **SettingsViewModel**: 设置管理逻辑
- **DeviceViewModel**: 设备管理逻辑

#### Repository层
- **AuthRepository**: 用户认证数据仓库
- **CameraRepository**: 摄像头数据仓库
- **ViewerRepository**: 查看端数据仓库
- **DeviceRepository**: 设备管理数据仓库
- **OfflineRepository**: 离线数据同步仓库

#### 数据层
- **Room Database**: 本地数据存储
- **DataStore**: 用户设置存储
- **Network Service**: 网络请求封装
- **WorkManager**: 后台任务处理
- **TensorFlow Lite**: 本地AI推理

#### 服务层
- **CameraService**: 摄像头服务
- **WebSocketService**: 实时通信服务
- **NotificationService**: 推送通知服务
- **OfflineSyncService**: 离线同步服务
- **AIProcessingService**: AI识别服务

## 使用流程

### 用户注册和登录
1. **首次使用**: 用户注册账号，设置用户名和密码
2. **登录验证**: JWT token认证，支持自动登录
3. **设备绑定**: 将设备与用户账号绑定

### 采集端使用流程
1. **选择采集模式**: 用户选择"采集"模式
2. **摄像头初始化**: 启动Camera2 API，配置视频参数
3. **AI模型加载**: 加载TensorFlow Lite模型（哭声检测等）
4. **连接服务器**: 建立WebSocket连接
5. **实时采集**: 
   - 视频流实时编码和传输
   - 本地AI识别处理
   - 异常事件检测和通知
6. **离线处理**: 网络断开时本地录制，网络恢复后自动上传

### 查看端使用流程
1. **选择查看模式**: 用户选择"查看"模式
2. **设备选择**: 选择要查看的采集设备
3. **建立连接**: 连接WebSocket接收视频流
4. **实时查看**: 
   - 接收并显示视频流
   - 接收AI识别结果和通知
   - 远程控制采集设备
   - 🎤 双向语音对讲（与家人/宠物实时通话）
5. **历史回放**: 查看历史录制视频

### 离线数据同步
1. **数据缓存**: 离线时数据存储在本地Room数据库
2. **WorkManager处理**: 后台任务定期尝试同步数据
3. **智能重试**: 网络恢复后自动同步离线数据
4. **冲突解决**: 处理数据冲突和版本控制

## 安装和运行

### 后端启动
```bash
cd backend
pip install -r requirements.txt
# 启动MySQL数据库
sudo systemctl start mysql
# 创建数据库
mysql -u root -p -e "CREATE DATABASE baby_monitor;"
# 启动Redis (用于缓存和会话管理)
redis-server
# 启动FastAPI服务
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Android应用
1. 使用Android Studio打开android目录
2. 连接Android设备或启动模拟器
3. 配置服务器地址（默认: http://localhost:8000）
4. 运行应用

## 配置说明

### 后端配置
- **默认端口**: 8000
- **WebSocket路径**: `/ws/{device_id}`
- **视频流格式**: MJPEG/H.264
- **AI模型路径**: `models/` 目录
- **Redis配置**: 默认端口6379
- **数据库**: MySQL 8.0+

### Android配置
- **最低SDK版本**: 21 (Android 5.0)
- **目标SDK版本**: 34
- **权限**: CAMERA, INTERNET, RECORD_AUDIO, WAKE_LOCK
- **TensorFlow Lite**: 支持CPU/GPU推理
- **WorkManager**: 后台任务处理
- **DataStore**: 用户设置存储

### AI模型配置
- **哭声检测模型**: `baby_cry_detection.tflite`
- **宠物行为识别**: `pet_behavior.tflite`
- **人脸识别**: `face_detection.tflite`
- **模型更新**: 支持在线更新模型文件

## 开发计划

### 第一阶段 - 基础功能
- [x] 项目架构设计
- [ ] FastAPI后端开发
- [ ] 用户认证和授权系统
- [ ] 设备管理和绑定
- [ ] 基础WebSocket通信

### 第二阶段 - 核心功能
- [ ] Android采集端开发
- [ ] Android查看端开发
- [ ] 实时视频流传输
- [ ] Room数据库集成
- [ ] 基础UI界面

### 第三阶段 - 离线支持
- [ ] WorkManager后台任务
- [ ] 离线数据同步机制
- [ ] 本地视频录制和缓存
- [ ] 数据冲突解决
- [ ] 网络状态监控

### 第四阶段 - AI集成
- [ ] TensorFlow Lite集成
- [ ] 哭声检测模型
- [ ] 宠物行为识别
- [ ] 人脸识别功能
- [ ] 异常事件检测

### 第四阶段 - 语音对讲功能
- [ ] WebRTC音频通信集成
- [ ] 双向语音对讲实现
- [ ] 音频质量优化
- [ ] 噪音抑制和回声消除
- [ ] 语音对讲UI界面

### 第五阶段 - 高级功能
- [ ] 推送通知系统
- [ ] 云端存储集成
- [ ] 历史数据回放
- [ ] 远程设备控制
- [ ] 数据分析和统计

### 第六阶段 - 优化和部署
- [ ] 性能优化
- [ ] 安全性加固
- [ ] 测试和调试
- [ ] 文档完善
- [ ] 生产环境部署

## API接口文档

### 用户认证接口
```
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
POST /api/auth/refresh
GET  /api/auth/profile
PUT  /api/auth/profile
```

### 设备管理接口
```
GET    /api/devices                    # 获取用户设备列表
POST   /api/devices                    # 注册新设备
GET    /api/devices/{device_id}        # 获取设备详情
PUT    /api/devices/{device_id}        # 更新设备信息
DELETE /api/devices/{device_id}        # 删除设备
POST   /api/devices/{device_id}/bind   # 绑定设备
POST   /api/devices/{device_id}/unbind # 解绑设备
```

### 视频流接口
```
WebSocket /ws/camera/{device_id}       # 摄像头视频流
WebSocket /ws/viewer/{device_id}       # 查看端连接
GET      /api/streams/{device_id}      # 获取视频流状态
POST     /api/streams/{device_id}/start # 开始视频流
POST     /api/streams/{device_id}/stop  # 停止视频流
```

### 语音对讲接口
```
WebSocket /ws/audio/{device_id}        # 音频流连接
POST     /api/audio/start_talk         # 开始语音对讲
POST     /api/audio/stop_talk          # 停止语音对讲
GET      /api/audio/status/{device_id} # 获取对讲状态
POST     /api/audio/mute               # 静音/取消静音
POST     /api/audio/volume             # 调节音量
```

### AI识别接口
```
POST /api/ai/detect/cry               # 哭声检测
POST /api/ai/detect/behavior          # 行为识别
POST /api/ai/detect/face              # 人脸识别
GET  /api/ai/models                   # 获取AI模型列表
POST /api/ai/models/update            # 更新AI模型
```

### 离线数据接口
```
GET  /api/sync/offline                # 获取离线数据
POST /api/sync/upload                 # 上传离线数据
GET  /api/sync/status                 # 获取同步状态
POST /api/sync/conflict/resolve       # 解决数据冲突
```

### 通知接口
```
GET  /api/notifications               # 获取通知列表
POST /api/notifications/mark_read     # 标记通知已读
POST /api/notifications/send          # 发送通知
```

### 家庭管理接口
```
GET    /api/families                  # 获取家庭列表
POST   /api/families                  # 创建家庭
GET    /api/families/{family_id}      # 获取家庭详情
PUT    /api/families/{family_id}      # 更新家庭信息
DELETE /api/families/{family_id}      # 删除家庭
POST   /api/families/{family_id}/members # 添加家庭成员
DELETE /api/families/{family_id}/members/{user_id} # 移除家庭成员
```

### 健康数据接口
```
GET  /api/health/sleep/{device_id}    # 获取睡眠数据
POST /api/health/sleep                # 记录睡眠数据
GET  /api/health/feeding/{device_id}  # 获取喂养记录
POST /api/health/feeding              # 记录喂养数据
GET  /api/health/activity/{device_id} # 获取活动数据
POST /api/health/activity             # 记录活动数据
GET  /api/health/temperature/{device_id} # 获取体温数据
POST /api/health/temperature          # 记录体温数据
```

### 日程管理接口
```
GET    /api/schedules                 # 获取日程列表
POST   /api/schedules                 # 创建日程
PUT    /api/schedules/{schedule_id}   # 更新日程
DELETE /api/schedules/{schedule_id}   # 删除日程
GET    /api/schedules/reminders       # 获取提醒列表
POST   /api/schedules/reminders       # 创建提醒
```

### 媒体管理接口
```
GET  /api/media/videos/{device_id}    # 获取视频列表
POST /api/media/upload                # 上传视频
GET  /api/media/videos/{video_id}     # 获取视频详情
DELETE /api/media/videos/{video_id}   # 删除视频
GET  /api/media/screenshots/{device_id} # 获取截图列表
POST /api/media/screenshots           # 上传截图
```

### 设置管理接口
```
GET  /api/settings/user               # 获取用户设置
PUT  /api/settings/user               # 更新用户设置
GET  /api/settings/device/{device_id} # 获取设备设置
PUT  /api/settings/device/{device_id} # 更新设备设置
GET  /api/settings/ai                 # 获取AI设置
PUT  /api/settings/ai                 # 更新AI设置
```

## 数据库设计

### 用户表 (users)
- user_id (主键)
- username (用户名)
- email (邮箱)
- password_hash (密码哈希)
- display_name (显示名称)
- avatar (头像)
- is_logged_in (是否已登录)
- last_login_time (最后登录时间)
- created_at (创建时间)
- updated_at (更新时间)

### 设备表 (devices)
- device_id (主键)
- device_name (设备名称)
- device_type (设备类型: CAMERA/VIEWER)
- is_online (是否在线)
- last_seen (最后在线时间)
- server_url (服务器地址)
- is_paired (是否已配对)
- paired_device_id (配对设备ID)
- created_at (创建时间)
- updated_at (更新时间)

### 用户设备关联表 (user_devices)
- id (主键)
- user_id (用户ID)
- device_id (设备ID)
- device_name (设备名称)
- device_type (设备类型)
- is_owner (是否为所有者)
- permissions (权限)
- is_active (是否激活)
- added_at (添加时间)

### 连接日志表 (connection_logs)
- id (主键)
- device_id (设备ID)
- connection_type (连接类型)
- status (连接状态)
- start_time (开始时间)
- end_time (结束时间)
- duration (持续时间)
- error_message (错误信息)
- server_url (服务器地址)
- is_offline (是否离线)

### 离线数据表 (offline_data)
- id (主键)
- data_type (数据类型)
- device_id (设备ID)
- data (数据内容)
- is_synced (是否已同步)
- sync_attempts (同步尝试次数)
- last_sync_attempt (最后同步尝试时间)
- created_at (创建时间)
- priority (同步优先级)

### 家庭表 (families)
- family_id (主键)
- family_name (家庭名称)
- family_code (家庭邀请码)
- owner_id (家庭所有者ID)
- created_at (创建时间)
- updated_at (更新时间)

### 家庭成员表 (family_members)
- id (主键)
- family_id (家庭ID)
- user_id (用户ID)
- role (角色: OWNER/ADMIN/MEMBER/GUEST)
- permissions (权限)
- joined_at (加入时间)
- is_active (是否激活)

### 健康数据表 (health_data)
- id (主键)
- device_id (设备ID)
- data_type (数据类型: SLEEP/FEEDING/ACTIVITY/TEMPERATURE)
- value (数值)
- unit (单位)
- timestamp (时间戳)
- notes (备注)
- created_at (创建时间)

### 日程表 (schedules)
- schedule_id (主键)
- user_id (用户ID)
- device_id (设备ID)
- title (标题)
- description (描述)
- schedule_type (类型: FEEDING/SLEEP/ACTIVITY/REMINDER)
- start_time (开始时间)
- end_time (结束时间)
- repeat_type (重复类型: NONE/DAILY/WEEKLY/MONTHLY)
- is_active (是否激活)
- created_at (创建时间)
- updated_at (更新时间)

### 提醒表 (reminders)
- reminder_id (主键)
- schedule_id (日程ID)
- user_id (用户ID)
- reminder_time (提醒时间)
- message (提醒消息)
- is_sent (是否已发送)
- sent_at (发送时间)
- created_at (创建时间)

### 媒体文件表 (media_files)
- file_id (主键)
- device_id (设备ID)
- user_id (用户ID)
- file_type (文件类型: VIDEO/IMAGE/AUDIO)
- file_name (文件名)
- file_path (文件路径)
- file_size (文件大小)
- duration (时长，视频/音频)
- thumbnail_path (缩略图路径)
- is_processed (是否已处理)
- created_at (创建时间)

### 用户设置表 (user_settings)
- id (主键)
- user_id (用户ID)
- setting_key (设置键)
- setting_value (设置值)
- setting_type (设置类型: STRING/INTEGER/BOOLEAN/JSON)
- updated_at (更新时间)

### 设备设置表 (device_settings)
- id (主键)
- device_id (设备ID)
- setting_key (设置键)
- setting_value (设置值)
- setting_type (设置类型)
- updated_at (更新时间)

### AI检测记录表 (ai_detections)
- id (主键)
- device_id (设备ID)
- detection_type (检测类型: CRY/BEHAVIOR/FACE/TEMPERATURE)
- confidence (置信度)
- bounding_box (边界框坐标)
- detection_data (检测数据JSON)
- image_path (图片路径)
- video_path (视频路径)
- timestamp (时间戳)
- is_processed (是否已处理)
- created_at (创建时间)

### 语音对讲记录表 (audio_calls)
- id (主键)
- caller_device_id (呼叫方设备ID)
- receiver_device_id (接收方设备ID)
- call_type (通话类型: AUDIO/VIDEO)
- start_time (开始时间)
- end_time (结束时间)
- duration (通话时长)
- audio_quality (音频质量)
- status (通话状态: CONNECTING/CONNECTED/ENDED/FAILED)
- created_at (创建时间)

## WorkManager任务

### 离线数据同步任务
- **任务名称**: OfflineDataSyncWorker
- **触发条件**: 网络可用时
- **执行频率**: 每15分钟
- **重试策略**: 指数退避
- **约束条件**: 需要网络连接

### 视频上传任务
- **任务名称**: VideoUploadWorker
- **触发条件**: 检测到离线视频文件
- **执行频率**: 立即执行
- **重试策略**: 最多3次
- **约束条件**: 需要WiFi连接

### AI模型更新任务
- **任务名称**: ModelUpdateWorker
- **触发条件**: 服务器有新模型
- **执行频率**: 每天检查一次
- **重试策略**: 最多5次
- **约束条件**: 需要WiFi连接

### 健康数据同步任务
- **任务名称**: HealthDataSyncWorker
- **触发条件**: 有新的健康数据
- **执行频率**: 每小时执行一次
- **重试策略**: 最多3次
- **约束条件**: 需要网络连接

### 媒体文件处理任务
- **任务名称**: MediaProcessingWorker
- **触发条件**: 检测到新的媒体文件
- **执行频率**: 立即执行
- **重试策略**: 最多5次
- **约束条件**: 需要WiFi连接

### 提醒发送任务
- **任务名称**: ReminderWorker
- **触发条件**: 到达提醒时间
- **执行频率**: 每分钟检查一次
- **重试策略**: 最多2次
- **约束条件**: 无特殊要求

### 数据清理任务
- **任务名称**: DataCleanupWorker
- **触发条件**: 定期清理
- **执行频率**: 每天凌晨2点
- **重试策略**: 最多1次
- **约束条件**: 无特殊要求

### 音频处理任务
- **任务名称**: AudioProcessingWorker
- **触发条件**: 检测到音频文件
- **执行频率**: 立即执行
- **重试策略**: 最多3次
- **约束条件**: 需要网络连接

### 语音对讲任务
- **任务名称**: VoiceCallWorker
- **触发条件**: 语音对讲请求
- **执行频率**: 立即执行
- **重试策略**: 最多2次
- **约束条件**: 需要网络连接

## 安全性设计

### 数据加密
- **传输加密**: 所有API通信使用HTTPS/TLS 1.3
- **存储加密**: 敏感数据使用AES-256加密
- **端到端加密**: 视频流使用端到端加密
- **密钥管理**: 使用Android Keystore管理密钥

### 身份认证
- **JWT Token**: 访问令牌和刷新令牌机制
- **生物识别**: 指纹/面部识别登录
- **多因素认证**: 支持短信/邮箱验证
- **会话管理**: 自动过期和刷新机制

### 隐私保护
- **数据最小化**: 只收集必要数据
- **用户控制**: 用户可以控制数据使用
- **匿名化**: 敏感数据匿名化处理
- **GDPR合规**: 符合数据保护法规

### 网络安全
- **API限流**: 防止暴力攻击
- **输入验证**: 严格的输入验证和过滤
- **SQL注入防护**: 使用参数化查询
- **XSS防护**: 输出编码和CSP策略

## 性能优化

### 移动端优化
- **内存管理**: 优化内存使用，防止OOM
- **电池优化**: 智能后台任务调度
- **网络优化**: 请求合并和缓存策略
- **UI优化**: 60fps流畅动画

### 服务端优化
- **数据库优化**: 索引优化和查询优化
- **缓存策略**: Redis缓存热点数据
- **CDN加速**: 静态资源CDN分发
- **负载均衡**: 支持水平扩展

### 视频流优化
- **自适应码率**: 根据网络状况调整码率
- **硬件编码**: 使用硬件加速编码
- **帧率控制**: 智能帧率调整
- **缓冲策略**: 优化缓冲和延迟

## 监控和日志

### 应用监控
- **崩溃报告**: Firebase Crashlytics
- **性能监控**: Firebase Performance
- **用户行为**: 匿名使用统计
- **错误追踪**: 详细错误日志

### 服务端监控
- **系统监控**: CPU、内存、磁盘使用率
- **API监控**: 响应时间和错误率
- **数据库监控**: 查询性能和连接数
- **日志管理**: 结构化日志和日志轮转

## 部署和运维

### 容器化部署
- **Docker**: 应用容器化
- **Docker Compose**: 本地开发环境
- **Kubernetes**: 生产环境编排
- **CI/CD**: 自动化部署流水线

### 数据库管理
- **备份策略**: 定期自动备份
- **主从复制**: 读写分离
- **监控告警**: 数据库性能监控
- **版本管理**: 数据库迁移管理

## 贡献指南

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License
