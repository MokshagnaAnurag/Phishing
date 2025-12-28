package com.neura.frauddetection.models

import com.google.gson.annotations.SerializedName

/**
 * Scan Result Model - Response from API
 */
data class ScanResult(
    @SerializedName("is_fraud")
    val isFraud: Boolean,
    
    @SerializedName("confidence")
    val confidence: Float,
    
    @SerializedName("risk_level")
    val riskLevel: String,
    
    @SerializedName("message")
    val message: String,
    
    @SerializedName("details")
    val details: Map<String, Any>? = null
)


