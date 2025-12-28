package com.neura.frauddetection

import android.app.Application
import com.google.firebase.FirebaseApp

/**
 * Application class for Firebase initialization
 */
class NeuraApplication : Application() {
    
    override fun onCreate() {
        super.onCreate()
        
        // Initialize Firebase
        if (FirebaseApp.getApps(this).isEmpty()) {
            FirebaseApp.initializeApp(this)
        }
    }
}


