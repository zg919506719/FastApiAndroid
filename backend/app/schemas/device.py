from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.device import DeviceType

class DeviceBase(BaseModel):
    device_name: str
    device_type: DeviceType

class DeviceCreate(DeviceBase):
    device_id: str

class DeviceUpdate(BaseModel):
    device_name: Optional[str] = None
    server_url: Optional[str] = None

class DeviceResponse(DeviceBase):
    device_id: str
    is_online: bool
    last_seen: Optional[datetime]
    is_paired: bool
    paired_device_id: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
