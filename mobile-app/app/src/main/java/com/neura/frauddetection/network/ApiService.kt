package com.neura.frauddetection.network

import com.neura.frauddetection.models.ScanResult
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.POST
import com.google.gson.GsonBuilder
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor

/**
 * API Service Interface
 * Define all API endpoints
 */
interface ApiService {
    
    @POST("scan/sms")
    suspend fun scanSMS(
        @Body request: SMSRequest
    ): ScanResult
    
    @POST("scan/call")
    suspend fun scanCall(
        @Body request: CallRequest
    ): ScanResult
    
    @POST("scan/email")
    suspend fun scanEmail(
        @Body request: EmailRequest
    ): ScanResult
    
    @POST("scan/url")
    suspend fun scanURL(
        @Body request: URLRequest
    ): ScanResult
    
    companion object {
        // Change this to your backend URL
        private const val BASE_URL = "http://10.0.2.2:8000/"  // Android emulator localhost
        // For physical device: "http://YOUR_COMPUTER_IP:8000/"
        
        fun create(): ApiService {
            val gson = GsonBuilder()
                .setLenient()
                .create()
            
            val logging = HttpLoggingInterceptor()
            logging.level = HttpLoggingInterceptor.Level.BODY
            
            val client = OkHttpClient.Builder()
                .addInterceptor(logging)
                .build()
            
            val retrofit = Retrofit.Builder()
                .baseUrl(BASE_URL)
                .client(client)
                .addConverterFactory(GsonConverterFactory.create(gson))
                .build()
            
            return retrofit.create(ApiService::class.java)
        }
    }
}

// Request Models
data class SMSRequest(
    val text: String,
    val phone_number: String? = null
)

data class CallRequest(
    val phone_number: String,
    val call_duration: Int? = null
)

data class EmailRequest(
    val subject: String,
    val body: String,
    val sender: String? = null
)

data class URLRequest(
    val url: String
)


