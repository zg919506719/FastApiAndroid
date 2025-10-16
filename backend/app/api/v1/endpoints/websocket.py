from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_user_id_from_token
from app.websocket.manager import WebSocketManager
from app.models.device import Device
from app.models.user_device import UserDevice
import json

router = APIRouter()

# 创建WebSocket管理器实例
websocket_manager = WebSocketManager()

@router.websocket("/camera/{device_id}")
async def camera_websocket(websocket: WebSocket, device_id: str, token: str = None):
    """摄像头WebSocket连接"""
    # 验证设备是否存在
    # 这里可以添加设备验证逻辑
    
    await websocket_manager.connect(websocket, device_id)
    
    try:
        while True:
            # 接收消息
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # 处理不同类型的消息
            if message.get("type") == "video_frame":
                # 处理视频帧数据
                await handle_video_frame(device_id, message)
            elif message.get("type") == "heartbeat":
                # 处理心跳消息
                await handle_heartbeat(device_id, message)
            elif message.get("type") == "status_update":
                # 处理状态更新
                await handle_status_update(device_id, message)
            
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket, device_id)
    except Exception as e:
        print(f"WebSocket错误: {e}")
        websocket_manager.disconnect(websocket, device_id)

@router.websocket("/viewer/{device_id}")
async def viewer_websocket(websocket: WebSocket, device_id: str, token: str = None):
    """查看端WebSocket连接"""
    # 验证设备是否存在
    # 这里可以添加设备验证逻辑
    
    await websocket_manager.connect(websocket, device_id)
    
    try:
        while True:
            # 接收消息
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # 处理查看端消息
            if message.get("type") == "request_video":
                # 请求视频流
                await handle_video_request(device_id, message)
            elif message.get("type") == "control_command":
                # 控制命令
                await handle_control_command(device_id, message)
            elif message.get("type") == "heartbeat":
                # 心跳消息
                await handle_heartbeat(device_id, message)
            
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket, device_id)
    except Exception as e:
        print(f"WebSocket错误: {e}")
        websocket_manager.disconnect(websocket, device_id)

async def handle_video_frame(device_id: str, message: dict):
    """处理视频帧数据"""
    # 这里可以添加视频帧处理逻辑
    # 例如：保存到文件、AI分析等
    print(f"收到设备 {device_id} 的视频帧数据")

async def handle_heartbeat(device_id: str, message: dict):
    """处理心跳消息"""
    # 更新设备在线状态
    await websocket_manager.send_to_device(device_id, {
        "type": "heartbeat_response",
        "device_id": device_id,
        "timestamp": message.get("timestamp")
    })

async def handle_status_update(device_id: str, message: dict):
    """处理状态更新"""
    # 广播状态更新到所有查看端
    await websocket_manager.send_to_device(device_id, {
        "type": "status_update",
        "device_id": device_id,
        "status": message.get("status"),
        "timestamp": message.get("timestamp")
    })

async def handle_video_request(device_id: str, message: dict):
    """处理视频请求"""
    # 转发视频请求到摄像头设备
    await websocket_manager.send_to_device(device_id, {
        "type": "start_video_stream",
        "request_id": message.get("request_id"),
        "quality": message.get("quality", "medium")
    })

async def handle_control_command(device_id: str, message: dict):
    """处理控制命令"""
    # 转发控制命令到摄像头设备
    await websocket_manager.send_to_device(device_id, {
        "type": "control_command",
        "command": message.get("command"),
        "parameters": message.get("parameters", {})
    })

@router.get("/status/{device_id}")
async def get_device_status(device_id: str):
    """获取设备连接状态"""
    is_online = websocket_manager.is_device_online(device_id)
    connection_count = websocket_manager.get_device_connection_count(device_id)
    
    return {
        "device_id": device_id,
        "is_online": is_online,
        "connection_count": connection_count
    }

@router.get("/stats")
async def get_websocket_stats():
    """获取WebSocket统计信息"""
    return {
        "total_connections": websocket_manager.get_connection_count(),
        "active_devices": len(websocket_manager.device_connections),
        "active_users": len(websocket_manager.user_connections)
    }
