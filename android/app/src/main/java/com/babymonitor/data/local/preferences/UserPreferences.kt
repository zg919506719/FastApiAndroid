package com.babymonitor.data.local.preferences

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "user_preferences")

class UserPreferences(private val context: Context) {
    
    companion object {
        private val IS_LOGGED_IN = booleanPreferencesKey("is_logged_in")
        private val USER_ID = stringPreferencesKey("user_id")
        private val USERNAME = stringPreferencesKey("username")
        private val EMAIL = stringPreferencesKey("email")
        private val DISPLAY_NAME = stringPreferencesKey("display_name")
        private val ACCESS_TOKEN = stringPreferencesKey("access_token")
        private val REFRESH_TOKEN = stringPreferencesKey("refresh_token")
        private val DEVICE_ID = stringPreferencesKey("device_id")
        private val SERVER_URL = stringPreferencesKey("server_url")
    }
    
    val isLoggedIn: Flow<Boolean> = context.dataStore.data.map { preferences ->
        preferences[IS_LOGGED_IN] ?: false
    }
    
    val userId: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[USER_ID] ?: ""
    }
    
    val username: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[USERNAME] ?: ""
    }
    
    val email: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[EMAIL] ?: ""
    }
    
    val displayName: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[DISPLAY_NAME] ?: ""
    }
    
    val accessToken: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[ACCESS_TOKEN] ?: ""
    }
    
    val refreshToken: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[REFRESH_TOKEN] ?: ""
    }
    
    val deviceId: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[DEVICE_ID] ?: ""
    }
    
    val serverUrl: Flow<String> = context.dataStore.data.map { preferences ->
        preferences[SERVER_URL] ?: "http://10.0.2.2:8000"
    }
    
    suspend fun setLoggedIn(isLoggedIn: Boolean) {
        context.dataStore.edit { preferences ->
            preferences[IS_LOGGED_IN] = isLoggedIn
        }
    }
    
    suspend fun setUserInfo(
        userId: String,
        username: String,
        email: String,
        displayName: String
    ) {
        context.dataStore.edit { preferences ->
            preferences[USER_ID] = userId
            preferences[USERNAME] = username
            preferences[EMAIL] = email
            preferences[DISPLAY_NAME] = displayName
        }
    }
    
    suspend fun setTokens(accessToken: String, refreshToken: String) {
        context.dataStore.edit { preferences ->
            preferences[ACCESS_TOKEN] = accessToken
            preferences[REFRESH_TOKEN] = refreshToken
        }
    }
    
    suspend fun setDeviceId(deviceId: String) {
        context.dataStore.edit { preferences ->
            preferences[DEVICE_ID] = deviceId
        }
    }
    
    suspend fun setServerUrl(serverUrl: String) {
        context.dataStore.edit { preferences ->
            preferences[SERVER_URL] = serverUrl
        }
    }
    
    suspend fun clearUserData() {
        context.dataStore.edit { preferences ->
            preferences.clear()
        }
    }
    
    // 同步方法用于快速访问
    suspend fun isLoggedIn(): Boolean {
        return isLoggedIn.map { it }.let { flow ->
            // 这里需要在实际使用中处理Flow
            false // 临时返回值
        }
    }
}
