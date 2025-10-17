from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.v1.endpoints.auth import oauth2_scheme
from app.core.database import get_db
from app.core.security import get_user_id_from_token
from app.models.device import Device, DeviceType
from app.models.user_device import UserDevice
from app.schemas.device import DeviceCreate, DeviceResponse, DeviceUpdate

router = APIRouter()

@router.get("/", response_model=List[DeviceResponse])
async def get_user_devices(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """获取用户的设备列表"""
    user_id = get_user_id_from_token(token)
    
    # 获取用户关联的设备
    user_devices = db.query(UserDevice).filter(
        UserDevice.user_id == user_id,
        UserDevice.is_active == True
    ).all()
    
    devices = []
    for user_device in user_devices:
        device = db.query(Device).filter(Device.device_id == user_device.device_id).first()
        if device:
            devices.append(DeviceResponse(
                device_id=device.device_id,
                device_name=device.device_name,
                device_type=device.device_type,
                is_online=device.is_online,
                last_seen=device.last_seen,
                is_paired=device.is_paired,
                paired_device_id=device.paired_device_id,
                created_at=device.created_at
            ))
    
    return devices

@router.post("/", response_model=DeviceResponse)
async def create_device(
    device_data: DeviceCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """注册新设备"""
    user_id = get_user_id_from_token(token)
    
    # 检查设备ID是否已存在
    if db.query(Device).filter(Device.device_id == device_data.device_id).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="设备ID已存在"
        )
    
    # 创建设备
    device = Device(
        device_id=device_data.device_id,
        device_name=device_data.device_name,
        device_type=device_data.device_type
    )
    
    db.add(device)
    db.commit()
    db.refresh(device)
    
    # 创建用户设备关联
    user_device = UserDevice(
        user_id=user_id,
        device_id=device.device_id,
        device_name=device.device_name,
        device_type=device_data.device_type.value,
        is_owner=True,
        permissions="ADMIN"
    )
    
    db.add(user_device)
    db.commit()
    
    return DeviceResponse(
        device_id=device.device_id,
        device_name=device.device_name,
        device_type=device.device_type,
        is_online=device.is_online,
        last_seen=device.last_seen,
        is_paired=device.is_paired,
        paired_device_id=device.paired_device_id,
        created_at=device.created_at
    )

@router.get("/{device_id}", response_model=DeviceResponse)
async def get_device(
    device_id: str,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """获取设备详情"""
    user_id = get_user_id_from_token(token)
    
    # 检查用户是否有权限访问该设备
    user_device = db.query(UserDevice).filter(
        UserDevice.user_id == user_id,
        UserDevice.device_id == device_id,
        UserDevice.is_active == True
    ).first()
    
    if not user_device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在或无权限访问"
        )
    
    device = db.query(Device).filter(Device.device_id == device_id).first()
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在"
        )
    
    return DeviceResponse(
        device_id=device.device_id,
        device_name=device.device_name,
        device_type=device.device_type,
        is_online=device.is_online,
        last_seen=device.last_seen,
        is_paired=device.is_paired,
        paired_device_id=device.paired_device_id,
        created_at=device.created_at
    )

@router.put("/{device_id}", response_model=DeviceResponse)
async def update_device(
    device_id: str,
    device_data: DeviceUpdate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """更新设备信息"""
    user_id = get_user_id_from_token(token)
    
    # 检查用户是否有权限修改该设备
    user_device = db.query(UserDevice).filter(
        UserDevice.user_id == user_id,
        UserDevice.device_id == device_id,
        UserDevice.is_active == True
    ).first()
    
    if not user_device or user_device.permissions not in ["ADMIN", "WRITE"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限修改该设备"
        )
    
    device = db.query(Device).filter(Device.device_id == device_id).first()
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在"
        )
    
    # 更新设备信息
    if device_data.device_name:
        device.device_name = device_data.device_name
    if device_data.server_url:
        device.server_url = device_data.server_url
    
    db.commit()
    db.refresh(device)
    
    return DeviceResponse(
        device_id=device.device_id,
        device_name=device.device_name,
        device_type=device.device_type,
        is_online=device.is_online,
        last_seen=device.last_seen,
        is_paired=device.is_paired,
        paired_device_id=device.paired_device_id,
        created_at=device.created_at
    )

@router.delete("/{device_id}")
async def delete_device(
    device_id: str,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """删除设备"""
    user_id = get_user_id_from_token(token)
    
    # 检查用户是否有权限删除该设备
    user_device = db.query(UserDevice).filter(
        UserDevice.user_id == user_id,
        UserDevice.device_id == device_id,
        UserDevice.is_active == True
    ).first()
    
    if not user_device or not user_device.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限删除该设备"
        )
    
    # 删除用户设备关联
    db.query(UserDevice).filter(UserDevice.device_id == device_id).delete()
    
    # 删除设备
    db.query(Device).filter(Device.device_id == device_id).delete()
    
    db.commit()
    
    return {"message": "设备删除成功"}

@router.post("/{device_id}/bind")
async def bind_device(
    device_id: str,
    paired_device_id: str,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """绑定设备"""
    user_id = get_user_id_from_token(token)
    
    # 检查用户是否有权限操作该设备
    user_device = db.query(UserDevice).filter(
        UserDevice.user_id == user_id,
        UserDevice.device_id == device_id,
        UserDevice.is_active == True
    ).first()
    
    if not user_device or user_device.permissions not in ["ADMIN", "WRITE"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限操作该设备"
        )
    
    # 检查配对设备是否存在
    paired_device = db.query(Device).filter(Device.device_id == paired_device_id).first()
    if not paired_device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="配对设备不存在"
        )
    
    # 更新设备绑定状态
    device = db.query(Device).filter(Device.device_id == device_id).first()
    device.is_paired = True
    device.paired_device_id = paired_device_id
    
    paired_device.is_paired = True
    paired_device.paired_device_id = device_id
    
    db.commit()
    
    return {"message": "设备绑定成功"}

@router.post("/{device_id}/unbind")
async def unbind_device(
    device_id: str,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """解绑设备"""
    user_id = get_user_id_from_token(token)
    
    # 检查用户是否有权限操作该设备
    user_device = db.query(UserDevice).filter(
        UserDevice.user_id == user_id,
        UserDevice.device_id == device_id,
        UserDevice.is_active == True
    ).first()
    
    if not user_device or user_device.permissions not in ["ADMIN", "WRITE"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限操作该设备"
        )
    
    # 更新设备绑定状态
    device = db.query(Device).filter(Device.device_id == device_id).first()
    if device.is_paired and device.paired_device_id:
        paired_device = db.query(Device).filter(Device.device_id == device.paired_device_id).first()
        if paired_device:
            paired_device.is_paired = False
            paired_device.paired_device_id = None
    
    device.is_paired = False
    device.paired_device_id = None
    
    db.commit()
    
    return {"message": "设备解绑成功"}
