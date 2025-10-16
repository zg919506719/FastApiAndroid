from sqlalchemy import Column, String, Boolean, DateTime, Text, Enum
from sqlalchemy.dialects.mysql import VARCHAR, TEXT, ENUM
from sqlalchemy.sql import func
from app.core.database import Base
import enum

class DeviceType(str, enum.Enum):
    CAMERA = "CAMERA"
    VIEWER = "VIEWER"

class Device(Base):
    __tablename__ = "devices"
    
    device_id = Column(VARCHAR(36), primary_key=True, index=True)
    device_name = Column(VARCHAR(100), nullable=False)
    device_type = Column(ENUM(DeviceType), nullable=False)
    is_online = Column(Boolean, default=False)
    last_seen = Column(DateTime, nullable=True)
    server_url = Column(VARCHAR(255), nullable=True)
    is_paired = Column(Boolean, default=False)
    paired_device_id = Column(VARCHAR(36), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
