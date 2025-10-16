package com.babymonitor.data.network

import com.babymonitor.data.model.*
import retrofit2.Response
import retrofit2.http.*

interface ApiService {
    
    // 用户认证
    @POST("auth/register")
    suspend fun register(@Body request: RegisterRequest): Response<AuthResponse>
    
    @POST("auth/login")
    suspend fun login(@Body request: LoginRequest): Response<AuthResponse>
    
    @POST("auth/refresh")
    suspend fun refreshToken(@Body refreshToken: String): Response<AuthResponse>
    
    @POST("auth/logout")
    suspend fun logout(@Header("Authorization") token: String): Response<Map<String, String>>
    
    @GET("auth/profile")
    suspend fun getProfile(@Header("Authorization") token: String): Response<User>
    
    // 设备管理
    @GET("devices/")
    suspend fun getDevices(@Header("Authorization") token: String): Response<List<Device>>
    
    @POST("devices/")
    suspend fun createDevice(
        @Header("Authorization") token: String,
        @Body request: DeviceCreateRequest
    ): Response<Device>
    
    @GET("devices/{device_id}")
    suspend fun getDevice(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Device>
    
    @PUT("devices/{device_id}")
    suspend fun updateDevice(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String,
        @Body request: DeviceUpdateRequest
    ): Response<Device>
    
    @DELETE("devices/{device_id}")
    suspend fun deleteDevice(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Map<String, String>>
    
    @POST("devices/{device_id}/bind")
    suspend fun bindDevice(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String,
        @Body pairedDeviceId: String
    ): Response<Map<String, String>>
    
    @POST("devices/{device_id}/unbind")
    suspend fun unbindDevice(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Map<String, String>>
    
    // 视频流
    @GET("streams/{device_id}")
    suspend fun getStreamStatus(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Map<String, Any>>
    
    @POST("streams/{device_id}/start")
    suspend fun startStream(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Map<String, String>>
    
    @POST("streams/{device_id}/stop")
    suspend fun stopStream(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Map<String, String>>
    
    // 语音对讲
    @POST("audio/start_talk")
    suspend fun startTalk(
        @Header("Authorization") token: String,
        @Body request: Map<String, String>
    ): Response<Map<String, String>>
    
    @POST("audio/stop_talk")
    suspend fun stopTalk(
        @Header("Authorization") token: String,
        @Body request: Map<String, String>
    ): Response<Map<String, String>>
    
    @GET("audio/status/{device_id}")
    suspend fun getAudioStatus(
        @Header("Authorization") token: String,
        @Path("device_id") deviceId: String
    ): Response<Map<String, Any>>
    
    @POST("audio/mute")
    suspend fun muteAudio(
        @Header("Authorization") token: String,
        @Body request: Map<String, Any>
    ): Response<Map<String, String>>
    
    @POST("audio/volume")
    suspend fun setVolume(
        @Header("Authorization") token: String,
        @Body request: Map<String, Any>
    ): Response<Map<String, String>>
}
