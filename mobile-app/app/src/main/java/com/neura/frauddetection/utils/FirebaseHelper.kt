package com.neura.frauddetection.utils

import com.google.firebase.firestore.FirebaseFirestore
import com.neura.frauddetection.models.ScanHistoryItem
import com.neura.frauddetection.models.ScanResult
import kotlinx.coroutines.tasks.await

/**
 * Firebase Helper - Handles Firestore operations
 */
class FirebaseHelper {
    
    private val db = FirebaseFirestore.getInstance()
    private val collectionName = "scan_history"
    
    /**
     * Save scan result to Firestore
     */
    suspend fun saveScanHistory(
        scanType: String,
        result: ScanResult,
        timestamp: Long
    ) {
        try {
            val data = hashMapOf(
                "scanType" to scanType,
                "isFraud" to result.isFraud,
                "confidence" to result.confidence,
                "riskLevel" to result.riskLevel,
                "message" to result.message,
                "timestamp" to timestamp
            )
            
            db.collection(collectionName)
                .add(data)
                .await()
        } catch (e: Exception) {
            // Log error - in production, use proper logging
            e.printStackTrace()
        }
    }
    
    /**
     * Get scan history from Firestore
     */
    suspend fun getScanHistory(): List<ScanHistoryItem> {
        return try {
            val snapshot = db.collection(collectionName)
                .orderBy("timestamp", com.google.firebase.firestore.Query.Direction.DESCENDING)
                .limit(50)
                .get()
                .await()
            
            snapshot.documents.map { doc ->
                ScanHistoryItem(
                    id = doc.id,
                    scanType = doc.getString("scanType") ?: "",
                    isFraud = doc.getBoolean("isFraud") ?: false,
                    confidence = (doc.getDouble("confidence") ?: 0.0).toFloat(),
                    riskLevel = doc.getString("riskLevel") ?: "LOW",
                    message = doc.getString("message") ?: "",
                    timestamp = doc.getLong("timestamp") ?: System.currentTimeMillis()
                )
            }
        } catch (e: Exception) {
            e.printStackTrace()
            emptyList()
        }
    }
    
    /**
     * Delete scan history item
     */
    suspend fun deleteHistoryItem(itemId: String) {
        try {
            db.collection(collectionName)
                .document(itemId)
                .delete()
                .await()
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
}


