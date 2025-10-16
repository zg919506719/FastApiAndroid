package com.babymonitor.data.model

import java.util.Date

/**
 * 用户数据模型
 */
data class User(
    val userId: String,
    val username: String,
    val email: String,
    val displayName: String? = null,
    val avatar: String? = null,
    val isLoggedIn: Boolean = false,
    val lastLoginTime: Date? = null,
    val createdAt: Date = Date()
)

/**
 * 登录请求
 */
data class LoginRequest(
    val username: String,
    val password: String,
    val rememberMe: Boolean = false
)

/**
 * 注册请求
 */
data class RegisterRequest(
    val username: String,
    val email: String,
    val password: String,
    val displayName: String? = null
)

/**
 * 认证响应
 */
data class AuthResponse(
    val success: Boolean,
    val message: String? = null,
    val user: User? = null,
    val token: String? = null,
    val refreshToken: String? = null,
    val tokenExpiry: Long? = null
)

/**
 * 设备信息
 */
data class Device(
    val deviceId: String,
    val deviceName: String,
    val deviceType: String, // CAMERA or VIEWER
    val isOnline: Boolean = false,
    val lastSeen: String? = null,
    val isPaired: Boolean = false,
    val pairedDeviceId: String? = null,
    val createdAt: String? = null
)

/**
 * 设备创建请求
 */
data class DeviceCreateRequest(
    val deviceId: String,
    val deviceName: String,
    val deviceType: String
)

/**
 * 设备更新请求
 */
data class DeviceUpdateRequest(
    val deviceName: String? = null,
    val serverUrl: String? = null
)

/**
 * 用户设备关联
 */
data class UserDevice(
    val id: Long,
    val userId: String,
    val deviceId: String,
    val deviceName: String,
    val deviceType: String,
    val isOwner: Boolean,
    val permissions: String,
    val isActive: Boolean,
    val addedAt: String
)
