package com.neura.frauddetection

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.neura.frauddetection.activities.ScanActivity
import com.neura.frauddetection.activities.HistoryActivity
import com.neura.frauddetection.activities.SettingsActivity
import com.neura.frauddetection.databinding.ActivityMainBinding
import com.neura.frauddetection.utils.PermissionHelper

/**
 * Main Activity - Home Dashboard
 * Shows risk level, recent threats, and quick scan options
 */
class MainActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityMainBinding
    private val permissionHelper = PermissionHelper(this)
    
    companion object {
        private const val PERMISSION_REQUEST_CODE = 100
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupUI()
        checkPermissions()
    }
    
    private fun setupUI() {
        // Set risk level (mock data for demo)
        updateRiskLevel("LOW")
        
        // Setup click listeners
        binding.btnScanSMS.setOnClickListener {
            startScanActivity("SMS")
        }
        
        binding.btnScanCall.setOnClickListener {
            startScanActivity("CALL")
        }
        
        binding.btnScanEmail.setOnClickListener {
            startScanActivity("EMAIL")
        }
        
        binding.btnScanURL.setOnClickListener {
            startScanActivity("URL")
        }
        
        binding.btnViewHistory.setOnClickListener {
            startActivity(Intent(this, HistoryActivity::class.java))
        }
        
        binding.btnSettings.setOnClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
        }
        
        // Recent threats (mock data)
        updateRecentThreats()
    }
    
    private fun startScanActivity(scanType: String) {
        val intent = Intent(this, ScanActivity::class.java)
        intent.putExtra("SCAN_TYPE", scanType)
        startActivity(intent)
    }
    
    private fun updateRiskLevel(level: String) {
        binding.tvRiskLevel.text = level
        when (level) {
            "HIGH" -> {
                binding.tvRiskLevel.setTextColor(ContextCompat.getColor(this, android.R.color.holo_red_dark))
                binding.riskIndicator.setBackgroundColor(ContextCompat.getColor(this, android.R.color.holo_red_dark))
            }
            "MEDIUM" -> {
                binding.tvRiskLevel.setTextColor(ContextCompat.getColor(this, android.R.color.holo_orange_dark))
                binding.riskIndicator.setBackgroundColor(ContextCompat.getColor(this, android.R.color.holo_orange_dark))
            }
            "LOW" -> {
                binding.tvRiskLevel.setTextColor(ContextCompat.getColor(this, android.R.color.holo_green_dark))
                binding.riskIndicator.setBackgroundColor(ContextCompat.getColor(this, android.R.color.holo_green_dark))
            }
        }
    }
    
    private fun updateRecentThreats() {
        // Mock data - in production, fetch from database
        binding.tvRecentThreats.text = "3 threats detected in last 24 hours"
    }
    
    private fun checkPermissions() {
        val permissions = arrayOf(
            Manifest.permission.READ_SMS,
            Manifest.permission.RECEIVE_SMS,
            Manifest.permission.READ_PHONE_STATE
        )
        
        val missingPermissions = permissions.filter {
            ContextCompat.checkSelfPermission(this, it) != PackageManager.PERMISSION_GRANTED
        }
        
        if (missingPermissions.isNotEmpty()) {
            ActivityCompat.requestPermissions(
                this,
                missingPermissions.toTypedArray(),
                PERMISSION_REQUEST_CODE
            )
        }
    }
    
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        
        if (requestCode == PERMISSION_REQUEST_CODE) {
            val allGranted = grantResults.all { it == PackageManager.PERMISSION_GRANTED }
            if (allGranted) {
                Toast.makeText(this, "Permissions granted", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Some permissions are required for full functionality", Toast.LENGTH_LONG).show()
            }
        }
    }
}


