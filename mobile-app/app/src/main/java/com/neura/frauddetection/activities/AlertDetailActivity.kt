package com.neura.frauddetection.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.neura.frauddetection.R
import com.neura.frauddetection.databinding.ActivityAlertDetailBinding

/**
 * Alert Detail Activity - Show detailed information about a detected threat
 */
class AlertDetailActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityAlertDetailBinding
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAlertDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        val isFraud = intent.getBooleanExtra("IS_FRAUD", false)
        val message = intent.getStringExtra("MESSAGE") ?: ""
        val confidence = intent.getFloatExtra("CONFIDENCE", 0f)
        val riskLevel = intent.getStringExtra("RISK_LEVEL") ?: "LOW"
        
        displayAlert(isFraud, message, confidence, riskLevel)
    }
    
    private fun displayAlert(isFraud: Boolean, message: String, confidence: Float, riskLevel: String) {
        binding.tvAlertMessage.text = message
        binding.tvConfidence.text = "Confidence: ${(confidence * 100).toInt()}%"
        binding.tvRiskLevel.text = "Risk Level: $riskLevel"
        
        if (isFraud) {
            binding.alertContainer.setBackgroundColor(
                ContextCompat.getColor(this, android.R.color.holo_red_light)
            )
            binding.tvAlertTitle.text = "⚠️ FRAUD DETECTED"
        } else {
            binding.alertContainer.setBackgroundColor(
                ContextCompat.getColor(this, android.R.color.holo_green_light)
            )
            binding.tvAlertTitle.text = "✅ Safe"
        }
    }
}


