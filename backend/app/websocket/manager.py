from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict, List
import json
import asyncio
from datetime import datetime

class WebSocketManager:
    def __init__(self):
        # 存储活跃连接
        self.active_connections: Dict[str, WebSocket] = {}
        # 存储设备连接
        self.device_connections: Dict[str, List[WebSocket]] = {}
        # 存储用户连接
        self.user_connections: Dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, device_id: str, user_id: str = None):
        """建立WebSocket连接"""
        await websocket.accept()
        
        # 存储连接
        self.active_connections[device_id] = websocket
        
        # 添加到设备连接列表
        if device_id not in self.device_connections:
            self.device_connections[device_id] = []
        self.device_connections[device_id].append(websocket)
        
        # 如果提供了用户ID，添加到用户连接列表
        if user_id:
            if user_id not in self.user_connections:
                self.user_connections[user_id] = []
            self.user_connections[user_id].append(websocket)
        
        # 发送连接成功消息
        await self.send_personal_message({
            "type": "connection_established",
            "device_id": device_id,
            "timestamp": datetime.utcnow().isoformat()
        }, websocket)
    
    def disconnect(self, websocket: WebSocket, device_id: str, user_id: str = None):
        """断开WebSocket连接"""
        # 从活跃连接中移除
        if device_id in self.active_connections:
            del self.active_connections[device_id]
        
        # 从设备连接列表中移除
        if device_id in self.device_connections:
            if websocket in self.device_connections[device_id]:
                self.device_connections[device_id].remove(websocket)
            if not self.device_connections[device_id]:
                del self.device_connections[device_id]
        
        # 从用户连接列表中移除
        if user_id and user_id in self.user_connections:
            if websocket in self.user_connections[user_id]:
                self.user_connections[user_id].remove(websocket)
            if not self.user_connections[user_id]:
                del self.user_connections[user_id]
    
    async def send_personal_message(self, message: dict, websocket: WebSocket):
        """发送个人消息"""
        try:
            await websocket.send_text(json.dumps(message))
        except Exception as e:
            print(f"发送消息失败: {e}")
    
    async def send_to_device(self, device_id: str, message: dict):
        """发送消息到指定设备的所有连接"""
        if device_id in self.device_connections:
            for websocket in self.device_connections[device_id]:
                try:
                    await websocket.send_text(json.dumps(message))
                except Exception as e:
                    print(f"发送消息到设备 {device_id} 失败: {e}")
    
    async def send_to_user(self, user_id: str, message: dict):
        """发送消息到指定用户的所有连接"""
        if user_id in self.user_connections:
            for websocket in self.user_connections[user_id]:
                try:
                    await websocket.send_text(json.dumps(message))
                except Exception as e:
                    print(f"发送消息到用户 {user_id} 失败: {e}")
    
    async def broadcast_to_all(self, message: dict):
        """广播消息到所有连接"""
        for websocket in self.active_connections.values():
            try:
                await websocket.send_text(json.dumps(message))
            except Exception as e:
                print(f"广播消息失败: {e}")
    
    def get_connection_count(self) -> int:
        """获取当前连接数"""
        return len(self.active_connections)
    
    def get_device_connection_count(self, device_id: str) -> int:
        """获取指定设备的连接数"""
        return len(self.device_connections.get(device_id, []))
    
    def get_user_connection_count(self, user_id: str) -> int:
        """获取指定用户的连接数"""
        return len(self.user_connections.get(user_id, []))
    
    def is_device_online(self, device_id: str) -> bool:
        """检查设备是否在线"""
        return device_id in self.device_connections and len(self.device_connections[device_id]) > 0
