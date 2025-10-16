from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.core.database import get_db
from app.core.security import (
    verify_password, 
    get_password_hash, 
    create_access_token, 
    create_refresh_token,
    verify_token,
    get_user_id_from_token
)
from app.models.user import User
from app.schemas.auth import UserCreate, UserLogin, UserResponse, TokenResponse
from app.core.config import settings
import uuid

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """用户注册"""
    # 检查用户名是否已存在
    if db.query(User).filter(User.username == user_data.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名已存在"
        )
    
    # 检查邮箱是否已存在
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="邮箱已存在"
        )
    
    # 创建新用户
    hashed_password = get_password_hash(user_data.password)
    user = User(
        user_id=str(uuid.uuid4()),
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password,
        display_name=user_data.display_name
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return UserResponse(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
        display_name=user.display_name,
        created_at=user.created_at
    )

@router.post("/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """用户登录"""
    # 验证用户
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 创建令牌
    access_token = create_access_token(data={"sub": user.user_id})
    refresh_token = create_refresh_token(data={"sub": user.user_id})
    
    # 更新用户登录状态
    user.is_logged_in = True
    user.last_login_time = datetime.utcnow()
    user.token = access_token
    user.token_expiry = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    user.refresh_token = refresh_token
    
    db.commit()
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    """刷新访问令牌"""
    try:
        payload = verify_token(refresh_token, "refresh")
        user_id = payload.get("sub")
        
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user or user.refresh_token != refresh_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="无效的刷新令牌"
            )
        
        # 创建新的访问令牌
        access_token = create_access_token(data={"sub": user.user_id})
        
        # 更新用户令牌
        user.token = access_token
        user.token_expiry = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        db.commit()
        
        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
        
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的刷新令牌"
        )

@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """用户登出"""
    user_id = get_user_id_from_token(token)
    
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        user.is_logged_in = False
        user.token = None
        user.token_expiry = None
        user.refresh_token = None
        db.commit()
    
    return {"message": "登出成功"}

@router.get("/profile", response_model=UserResponse)
async def get_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """获取用户信息"""
    user_id = get_user_id_from_token(token)
    
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return UserResponse(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
        display_name=user.display_name,
        created_at=user.created_at
    )
