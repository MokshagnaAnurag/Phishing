package com.neura.frauddetection.utils

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.provider.Telephony
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import com.neura.frauddetection.network.ApiService

/**
 * SMS Receiver - Automatically scan incoming SMS
 */
class SMSReceiver : BroadcastReceiver() {
    
    private val apiService = ApiService.create()
    
    override fun onReceive(context: Context, intent: Intent) {
        if (Telephony.Sms.Intents.SMS_RECEIVED_ACTION == intent.action) {
            val messages = Telephony.Sms.Intents.getMessagesFromIntent(intent)
            
            for (message in messages) {
                val messageBody = message.messageBody
                val senderPhone = message.originatingAddress
                
                Log.d("SMSReceiver", "Received SMS from $senderPhone: $messageBody")
                
                // Scan SMS in background
                CoroutineScope(Dispatchers.IO).launch {
                    try {
                        val result = apiService.scanSMS(messageBody, senderPhone)
                        
                        if (result.isFraud) {
                            // Show notification or alert
                            Log.w("SMSReceiver", "FRAUD DETECTED: ${result.message}")
                            // In production, show notification here
                        }
                    } catch (e: Exception) {
                        Log.e("SMSReceiver", "Error scanning SMS", e)
                    }
                }
            }
        }
    }
}


