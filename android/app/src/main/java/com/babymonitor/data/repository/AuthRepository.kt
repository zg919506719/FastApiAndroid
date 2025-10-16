package com.babymonitor.data.repository

import com.babymonitor.data.local.preferences.UserPreferences
import com.babymonitor.data.model.AuthResponse
import com.babymonitor.data.model.LoginRequest
import com.babymonitor.data.model.RegisterRequest
import com.babymonitor.data.model.User
import com.babymonitor.data.network.ApiService
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.first

class AuthRepository(
    private val apiService: ApiService,
    private val userPreferences: UserPreferences
) {
    
    suspend fun register(request: RegisterRequest): Result<AuthResponse> {
        return try {
            val response = apiService.register(request)
            if (response.isSuccessful) {
                val authResponse = response.body()!!
                if (authResponse.success) {
                    // 保存用户信息
                    authResponse.user?.let { user ->
                        userPreferences.setUserInfo(
                            userId = user.userId,
                            username = user.username,
                            email = user.email,
                            displayName = user.displayName ?: ""
                        )
                    }
                    
                    // 保存令牌
                    authResponse.token?.let { token ->
                        authResponse.refreshToken?.let { refreshToken ->
                            userPreferences.setTokens(token, refreshToken)
                        }
                    }
                    
                    userPreferences.setLoggedIn(true)
                }
                Result.success(authResponse)
            } else {
                Result.failure(Exception("注册失败: ${response.message()}"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
    
    suspend fun login(request: LoginRequest): Result<AuthResponse> {
        return try {
            val response = apiService.login(request)
            if (response.isSuccessful) {
                val authResponse = response.body()!!
                if (authResponse.success) {
                    // 保存用户信息
                    authResponse.user?.let { user ->
                        userPreferences.setUserInfo(
                            userId = user.userId,
                            username = user.username,
                            email = user.email,
                            displayName = user.displayName ?: ""
                        )
                    }
                    
                    // 保存令牌
                    authResponse.token?.let { token ->
                        authResponse.refreshToken?.let { refreshToken ->
                            userPreferences.setTokens(token, refreshToken)
                        }
                    }
                    
                    userPreferences.setLoggedIn(true)
                }
                Result.success(authResponse)
            } else {
                Result.failure(Exception("登录失败: ${response.message()}"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
    
    suspend fun logout(): Result<Unit> {
        return try {
            val token = userPreferences.accessToken.first()
            if (token.isNotEmpty()) {
                val response = apiService.logout("Bearer $token")
                if (response.isSuccessful) {
                    userPreferences.clearUserData()
                    Result.success(Unit)
                } else {
                    Result.failure(Exception("登出失败: ${response.message()}"))
                }
            } else {
                userPreferences.clearUserData()
                Result.success(Unit)
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
    
    suspend fun getProfile(): Result<User> {
        return try {
            val token = userPreferences.accessToken.first()
            if (token.isEmpty()) {
                return Result.failure(Exception("未登录"))
            }
            
            val response = apiService.getProfile("Bearer $token")
            if (response.isSuccessful) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("获取用户信息失败: ${response.message()}"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
    
    suspend fun refreshToken(): Result<AuthResponse> {
        return try {
            val refreshToken = userPreferences.refreshToken.first()
            if (refreshToken.isEmpty()) {
                return Result.failure(Exception("无刷新令牌"))
            }
            
            val response = apiService.refreshToken(refreshToken)
            if (response.isSuccessful) {
                val authResponse = response.body()!!
                if (authResponse.success) {
                    // 更新令牌
                    authResponse.token?.let { token ->
                        authResponse.refreshToken?.let { newRefreshToken ->
                            userPreferences.setTokens(token, newRefreshToken)
                        }
                    }
                }
                Result.success(authResponse)
            } else {
                Result.failure(Exception("刷新令牌失败: ${response.message()}"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
    
    fun isLoggedIn(): Flow<Boolean> = userPreferences.isLoggedIn
    fun getUserId(): Flow<String> = userPreferences.userId
    fun getUsername(): Flow<String> = userPreferences.username
    fun getEmail(): Flow<String> = userPreferences.email
    fun getDisplayName(): Flow<String> = userPreferences.displayName
    fun getAccessToken(): Flow<String> = userPreferences.accessToken
}
