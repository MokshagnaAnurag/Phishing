package com.neura.frauddetection.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.neura.frauddetection.databinding.ActivitySettingsBinding

/**
 * Settings Activity - App settings and configuration
 */
class SettingsActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivitySettingsBinding
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySettingsBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupUI()
    }
    
    private fun setupUI() {
        // Set app version
        binding.tvAppVersion.text = "Version 1.0.0"
        
        // Setup toggle switches (mock for demo)
        binding.switchAutoScan.isChecked = true
        binding.switchNotifications.isChecked = true
        
        // Setup click listeners
        binding.btnAbout.setOnClickListener {
            // Show about dialog
            android.app.AlertDialog.Builder(this)
                .setTitle("About NEURA")
                .setMessage("NEURA - Think Smart. Stay Safe.\n\nAI-Powered Fraud & Phishing Detection")
                .setPositiveButton("OK", null)
                .show()
        }
    }
}


