from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.dialects.mysql import VARCHAR, TEXT
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(VARCHAR(36), primary_key=True, index=True)
    username = Column(VARCHAR(50), unique=True, index=True, nullable=False)
    email = Column(VARCHAR(100), unique=True, index=True, nullable=False)
    password_hash = Column(VARCHAR(255), nullable=False)
    display_name = Column(VARCHAR(100), nullable=True)
    avatar = Column(TEXT, nullable=True)
    is_logged_in = Column(Boolean, default=False)
    last_login_time = Column(DateTime, nullable=True)
    token = Column(TEXT, nullable=True)
    token_expiry = Column(DateTime, nullable=True)
    refresh_token = Column(TEXT, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
