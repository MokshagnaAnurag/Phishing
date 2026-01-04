/**
 * Firebase Configuration
 * Replace these values with your Firebase project credentials
 * Get them from: Firebase Console > Project Settings > General > Your apps
 */

// Firebase configuration object
const firebaseConfig = {
    apiKey: "AIzaSyBXLMCa1F-qr-MYxP0raHXXWfAAa9fCOoc",
    authDomain: "fraud-phishing-detection-cadbf.firebaseapp.com",
    projectId: "fraud-phishing-detection-cadbf",
    storageBucket: "fraud-phishing-detection-cadbf.firebasestorage.app",
    messagingSenderId: "810197081216",
    appId: "1:810197081216:web:5c9756ea3fa5707d3a9a65",
    measurementId: "G-N7MH29FXZ4"
};


// Render backend URL - can be overridden by environment variable
const RENDER_API_URL = window.RENDER_API_URL || "https://fraud-phishing-detection-mobile-ixnh.onrender.com";

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { firebaseConfig, RENDER_API_URL };
}

