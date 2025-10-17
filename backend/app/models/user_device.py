from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey, INT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.device import DeviceType

class UserDevice(Base):
    __tablename__ = "user_devices"
    
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(VARCHAR(36), nullable=False, index=True)
    device_id = Column(VARCHAR(36), nullable=False, index=True)
    device_name = Column(VARCHAR(100), nullable=False)
    device_type = Column(VARCHAR(20), nullable=False)  # CAMERA or VIEWER
    is_owner = Column(Boolean, default=False)
    permissions = Column(VARCHAR(20), default="READ")
    is_active = Column(Boolean, default=True)
    added_at = Column(DateTime, default=func.now())
