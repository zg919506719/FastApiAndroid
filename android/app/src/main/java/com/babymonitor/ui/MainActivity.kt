package com.babymonitor.ui

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.babymonitor.databinding.ActivityMainBinding
import com.babymonitor.data.local.preferences.UserPreferences
import com.babymonitor.data.repository.AuthRepository
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityMainBinding
    private lateinit var authRepository: AuthRepository
    private lateinit var userPreferences: UserPreferences
    
    // 权限请求
    private val requestPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { permissions ->
        val allGranted = permissions.values.all { it }
        if (allGranted) {
            Toast.makeText(this, "权限已授予", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "需要摄像头和网络权限才能使用应用", Toast.LENGTH_LONG).show()
        }
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        // 初始化依赖
        initDependencies()
        
        setupUI()
        checkPermissions()
        checkLoginStatus()
    }
    
    private fun initDependencies() {
        // 这里应该通过依赖注入初始化
        // 暂时使用简单的初始化方式
        userPreferences = UserPreferences(this)
    }
    
    private fun setupUI() {
     /*   // 采集模式按钮
        binding.btnCameraMode.setOnClickListener {
            startActivity(Intent(this, CameraActivity::class.java))
        }
        
        // 查看模式按钮
        binding.btnViewerMode.setOnClickListener {
            startActivity(Intent(this, ViewerActivity::class.java))
        }
        
        // 设置按钮
        binding.btnSettings.setOnClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
        }
        
        // 登录按钮
        binding.btnLogin.setOnClickListener {
            startActivity(Intent(this, LoginActivity::class.java))
        }*/
    }
    
    private fun checkPermissions() {
        val permissions = arrayOf(
            Manifest.permission.CAMERA,
            Manifest.permission.INTERNET,
            Manifest.permission.ACCESS_NETWORK_STATE,
            Manifest.permission.RECORD_AUDIO,
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION
        )
        
        val permissionsToRequest = permissions.filter {
            ContextCompat.checkSelfPermission(this, it) != PackageManager.PERMISSION_GRANTED
        }
        
        if (permissionsToRequest.isNotEmpty()) {
            requestPermissionLauncher.launch(permissionsToRequest.toTypedArray())
        }
    }
    
    private fun checkLoginStatus() {
        CoroutineScope(Dispatchers.Main).launch {
            val isLoggedIn = userPreferences.isLoggedIn()
            if (isLoggedIn) {
                binding.btnLogin.text = "已登录"
                binding.btnLogin.isEnabled = false
            } else {
                binding.btnLogin.text = "登录"
                binding.btnLogin.isEnabled = true
            }
        }
    }
    
    override fun onResume() {
        super.onResume()
        checkLoginStatus()
    }
}
