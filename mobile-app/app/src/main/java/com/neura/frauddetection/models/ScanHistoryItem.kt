package com.neura.frauddetection.models

/**
 * Scan History Item Model - For displaying in history
 */
data class ScanHistoryItem(
    val id: String,
    val scanType: String,
    val isFraud: Boolean,
    val confidence: Float,
    val riskLevel: String,
    val message: String,
    val timestamp: Long
)


