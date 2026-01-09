package com.neura.frauddetection.activities

import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.neura.frauddetection.R
import com.neura.frauddetection.databinding.ActivityScanBinding
import com.neura.frauddetection.models.ScanResult
import com.neura.frauddetection.network.ApiService
import com.neura.frauddetection.network.SMSRequest
import com.neura.frauddetection.network.CallRequest
import com.neura.frauddetection.network.EmailRequest
import com.neura.frauddetection.network.URLRequest
import com.neura.frauddetection.utils.FirebaseHelper
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

/**
 * Scan Activity - Manual input and scan results
 * Supports SMS, Call, Email, and URL scanning
 */
class ScanActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityScanBinding
    private lateinit var scanType: String
    private val apiService = ApiService.create()
    private val firebaseHelper = FirebaseHelper()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityScanBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        scanType = intent.getStringExtra("SCAN_TYPE") ?: "SMS"
        
        setupUI()
    }
    
    private fun setupUI() {
        // Set title based on scan type
        binding.tvScanTitle.text = "Scan ${scanType}"
        
        // Show/hide relevant input fields
        when (scanType) {
            "SMS" -> {
                binding.layoutPhoneNumber.visibility = View.VISIBLE
                binding.layoutText.visibility = View.VISIBLE
                binding.layoutSubject.visibility = View.GONE
                binding.layoutBody.visibility = View.GONE
            }
            "CALL" -> {
                binding.layoutPhoneNumber.visibility = View.VISIBLE
                binding.layoutText.visibility = View.GONE
                binding.layoutSubject.visibility = View.GONE
                binding.layoutBody.visibility = View.GONE
            }
            "EMAIL" -> {
                binding.layoutPhoneNumber.visibility = View.GONE
                binding.layoutText.visibility = View.GONE
                binding.layoutSubject.visibility = View.VISIBLE
                binding.layoutBody.visibility = View.VISIBLE
            }
            "URL" -> {
                binding.layoutPhoneNumber.visibility = View.GONE
                binding.layoutText.visibility = View.VISIBLE
                binding.layoutSubject.visibility = View.GONE
                binding.layoutBody.visibility = View.GONE
            }
        }
        
        // Clear previous inputs
        binding.inputPhoneNumber.text?.clear()
        binding.inputText.text?.clear()
        binding.inputSubject.text?.clear()
        binding.inputBody.text?.clear()
        
        binding.btnScan.setOnClickListener {
            performScan()
        }
        
        binding.btnClear.setOnClickListener {
            clearInputs()
        }
    }
    
    private fun performScan() {
        binding.progressBar.visibility = View.VISIBLE
        binding.btnScan.isEnabled = false
        binding.resultContainer.visibility = View.GONE
        
        CoroutineScope(Dispatchers.IO).launch {
            try {
                val result = when (scanType) {
                    "SMS" -> {
                        val text = binding.inputText.text.toString()
                        val phone = binding.inputPhoneNumber.text.toString()
                        if (text.isEmpty()) {
                            throw IllegalArgumentException("SMS text cannot be empty")
                        }
                        apiService.scanSMS(SMSRequest(text, phone.ifEmpty { null }))
                    }
                    "CALL" -> {
                        val phone = binding.inputPhoneNumber.text.toString()
                        if (phone.isEmpty()) {
                            throw IllegalArgumentException("Phone number cannot be empty")
                        }
                        apiService.scanCall(CallRequest(phone, null))
                    }
                    "EMAIL" -> {
                        val subject = binding.inputSubject.text.toString()
                        val body = binding.inputBody.text.toString()
                        if (subject.isEmpty() || body.isEmpty()) {
                            throw IllegalArgumentException("Email subject and body cannot be empty")
                        }
                        apiService.scanEmail(EmailRequest(subject, body, null))
                    }
                    "URL" -> {
                        val url = binding.inputText.text.toString()
                        if (url.isEmpty()) {
                            throw IllegalArgumentException("URL cannot be empty")
                        }
                        apiService.scanURL(URLRequest(url))
                    }
                    else -> throw IllegalArgumentException("Unknown scan type")
                }
                
                withContext(Dispatchers.Main) {
                    displayResult(result)
                    saveToHistory(result)
                }
            } catch (e: Exception) {
                withContext(Dispatchers.Main) {
                    Toast.makeText(this@ScanActivity, "Error: ${e.message}", Toast.LENGTH_LONG).show()
                    binding.progressBar.visibility = View.GONE
                    binding.btnScan.isEnabled = true
                }
            }
        }
    }
    
    private fun displayResult(result: ScanResult) {
        binding.progressBar.visibility = View.GONE
        binding.btnScan.isEnabled = true
        binding.resultContainer.visibility = View.VISIBLE
        
        // Set result message
        binding.tvResultMessage.text = result.message
        
        // Set confidence
        binding.tvConfidence.text = "Confidence: ${(result.confidence * 100).toInt()}%"
        
        // Set risk level
        binding.tvRiskLevel.text = "Risk: ${result.riskLevel}"
        
        // Color coding
        if (result.isFraud) {
            binding.resultContainer.setBackgroundColor(
                ContextCompat.getColor(this, android.R.color.holo_red_light)
            )
            binding.tvResultMessage.setTextColor(
                ContextCompat.getColor(this, android.R.color.holo_red_dark)
            )
        } else {
            binding.resultContainer.setBackgroundColor(
                ContextCompat.getColor(this, android.R.color.holo_green_light)
            )
            binding.tvResultMessage.setTextColor(
                ContextCompat.getColor(this, android.R.color.holo_green_dark)
            )
        }
    }
    
    private fun saveToHistory(result: ScanResult) {
        CoroutineScope(Dispatchers.IO).launch {
            try {
                firebaseHelper.saveScanHistory(
                    scanType = scanType,
                    result = result,
                    timestamp = System.currentTimeMillis()
                )
            } catch (e: Exception) {
                // Log error but don't show to user
                e.printStackTrace()
            }
        }
    }
    
    private fun clearInputs() {
        binding.inputText.text.clear()
        binding.inputPhoneNumber.text.clear()
        binding.inputSubject.text.clear()
        binding.inputBody.text.clear()
        binding.resultContainer.visibility = View.GONE
    }
}

