package com.neura.frauddetection.adapters

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import com.neura.frauddetection.R
import com.neura.frauddetection.models.ScanHistoryItem
import java.text.SimpleDateFormat
import java.util.*

/**
 * RecyclerView Adapter for Scan History
 */
class ScanHistoryAdapter(
    private var historyItems: List<ScanHistoryItem>
) : RecyclerView.Adapter<ScanHistoryAdapter.ViewHolder>() {
    
    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvScanType: TextView = itemView.findViewById(R.id.tvScanType)
        val tvMessage: TextView = itemView.findViewById(R.id.tvMessage)
        val tvRiskLevel: TextView = itemView.findViewById(R.id.tvRiskLevel)
        val tvTimestamp: TextView = itemView.findViewById(R.id.tvTimestamp)
        val tvConfidence: TextView = itemView.findViewById(R.id.tvConfidence)
    }
    
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_scan_history, parent, false)
        return ViewHolder(view)
    }
    
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val item = historyItems[position]
        
        holder.tvScanType.text = item.scanType
        holder.tvMessage.text = item.message
        holder.tvRiskLevel.text = "Risk: ${item.riskLevel}"
        holder.tvConfidence.text = "Confidence: ${(item.confidence * 100).toInt()}%"
        
        // Format timestamp
        val dateFormat = SimpleDateFormat("MMM dd, yyyy HH:mm", Locale.getDefault())
        holder.tvTimestamp.text = dateFormat.format(Date(item.timestamp))
        
        // Color coding
        if (item.isFraud) {
            holder.tvRiskLevel.setTextColor(
                ContextCompat.getColor(holder.itemView.context, android.R.color.holo_red_dark)
            )
        } else {
            holder.tvRiskLevel.setTextColor(
                ContextCompat.getColor(holder.itemView.context, android.R.color.holo_green_dark)
            )
        }
    }
    
    override fun getItemCount(): Int = historyItems.size
    
    fun updateHistory(newHistory: List<ScanHistoryItem>) {
        historyItems = newHistory
        notifyDataSetChanged()
    }
}


