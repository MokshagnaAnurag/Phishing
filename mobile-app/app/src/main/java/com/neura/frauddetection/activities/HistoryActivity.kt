package com.neura.frauddetection.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.neura.frauddetection.R
import com.neura.frauddetection.adapters.ScanHistoryAdapter
import com.neura.frauddetection.databinding.ActivityHistoryBinding
import com.neura.frauddetection.models.ScanHistoryItem
import com.neura.frauddetection.utils.FirebaseHelper
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

/**
 * History Activity - Display scan history
 */
class HistoryActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityHistoryBinding
    private lateinit var adapter: ScanHistoryAdapter
    private val firebaseHelper = FirebaseHelper()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHistoryBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupRecyclerView()
        loadHistory()
    }
    
    private fun setupRecyclerView() {
        adapter = ScanHistoryAdapter(emptyList())
        binding.recyclerViewHistory.layoutManager = LinearLayoutManager(this)
        binding.recyclerViewHistory.adapter = adapter
    }
    
    private fun loadHistory() {
        binding.progressBar.visibility = android.view.View.VISIBLE
        
        CoroutineScope(Dispatchers.IO).launch {
            try {
                val history = firebaseHelper.getScanHistory()
                withContext(Dispatchers.Main) {
                    adapter.updateHistory(history)
                    binding.progressBar.visibility = android.view.View.GONE
                    
                    if (history.isEmpty()) {
                        binding.tvEmptyState.visibility = android.view.View.VISIBLE
                    } else {
                        binding.tvEmptyState.visibility = android.view.View.GONE
                    }
                }
            } catch (e: Exception) {
                withContext(Dispatchers.Main) {
                    binding.progressBar.visibility = android.view.View.GONE
                    // Show mock data for demo
                    val mockHistory = getMockHistory()
                    adapter.updateHistory(mockHistory)
                }
            }
        }
    }
    
    private fun getMockHistory(): List<ScanHistoryItem> {
        return listOf(
            ScanHistoryItem(
                id = "1",
                scanType = "SMS",
                isFraud = true,
                confidence = 0.85f,
                riskLevel = "HIGH",
                message = "URGENT: Your account will be suspended",
                timestamp = System.currentTimeMillis() - 3600000
            ),
            ScanHistoryItem(
                id = "2",
                scanType = "URL",
                isFraud = false,
                confidence = 0.92f,
                riskLevel = "LOW",
                message = "https://example.com",
                timestamp = System.currentTimeMillis() - 7200000
            ),
            ScanHistoryItem(
                id = "3",
                scanType = "EMAIL",
                isFraud = true,
                confidence = 0.78f,
                riskLevel = "MEDIUM",
                message = "Phishing email detected",
                timestamp = System.currentTimeMillis() - 10800000
            )
        )
    }
}


