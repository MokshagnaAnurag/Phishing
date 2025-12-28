"""
Threat Intelligence Integration
Optional module to enhance fraud detection with real-time threat data
"""
import requests
import time
from typing import Optional, Dict
import os


class ThreatIntelligence:
    """Integrate with threat intelligence APIs for enhanced detection"""
    
    def __init__(self):
        """Initialize threat intelligence services"""
        # API keys (set as environment variables in production)
        self.virustotal_api_key = os.getenv('VIRUSTOTAL_API_KEY')
        self.phishtank_api_key = os.getenv('PHISHTANK_API_KEY')
        self.enabled = bool(self.virustotal_api_key or self.phishtank_api_key)
    
    def check_url_reputation(self, url: str) -> Optional[Dict]:
        """
        Check URL against VirusTotal API
        
        Args:
            url: URL to check
            
        Returns:
            Dictionary with reputation data or None
        """
        if not self.virustotal_api_key:
            return None
        
        try:
            # VirusTotal API v3
            headers = {
                'x-apikey': self.virustotal_api_key
            }
            
            # Submit URL for analysis
            response = requests.post(
                'https://www.virustotal.com/vtapi/v2/url/scan',
                data={'url': url, 'apikey': self.virustotal_api_key},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'reputation': 'malicious' if data.get('positives', 0) > 0 else 'clean',
                    'detections': data.get('positives', 0),
                    'total_scans': data.get('total', 0),
                    'source': 'virustotal'
                }
        except Exception as e:
            print(f"VirusTotal API error: {e}")
        
        return None
    
    def check_phishing_url(self, url: str) -> Optional[Dict]:
        """
        Check URL against PhishTank API
        
        Args:
            url: URL to check
            
        Returns:
            Dictionary with phishing data or None
        """
        if not self.phishtank_api_key:
            return None
        
        try:
            # PhishTank API
            response = requests.post(
                'http://checkurl.phishtank.com/checkurl/',
                data={
                    'url': url,
                    'format': 'json',
                    'app_key': self.phishtank_api_key
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('results', {}).get('in_database'):
                    return {
                        'is_phishing': True,
                        'verified': data.get('results', {}).get('verified', False),
                        'source': 'phishtank'
                    }
        except Exception as e:
            print(f"PhishTank API error: {e}")
        
        return None
    
    def check_google_safe_browsing(self, url: str) -> Optional[Dict]:
        """
        Check URL against Google Safe Browsing API
        
        Args:
            url: URL to check
            
        Returns:
            Dictionary with safety data or None
        """
        api_key = os.getenv('GOOGLE_SAFE_BROWSING_API_KEY')
        if not api_key:
            return None
        
        try:
            # Google Safe Browsing API v4
            response = requests.post(
                f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}',
                json={
                    'client': {
                        'clientId': 'neura',
                        'clientVersion': '1.0'
                    },
                    'threatInfo': {
                        'threatTypes': ['MALWARE', 'SOCIAL_ENGINEERING'],
                        'platformTypes': ['ANY_PLATFORM'],
                        'threatEntryTypes': ['URL'],
                        'threatEntries': [{'url': url}]
                    }
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('matches'):
                    return {
                        'is_unsafe': True,
                        'threat_types': [m.get('threatType') for m in data.get('matches', [])],
                        'source': 'google_safe_browsing'
                    }
        except Exception as e:
            print(f"Google Safe Browsing API error: {e}")
        
        return None
    
    def enhanced_url_check(self, url: str) -> Dict:
        """
        Check URL against multiple threat intelligence sources
        
        Args:
            url: URL to check
            
        Returns:
            Combined threat intelligence results
        """
        results = {
            'threat_detected': False,
            'sources': [],
            'confidence_boost': 0.0
        }
        
        # Check VirusTotal
        vt_result = self.check_url_reputation(url)
        if vt_result:
            results['sources'].append('virustotal')
            if vt_result.get('reputation') == 'malicious':
                results['threat_detected'] = True
                results['confidence_boost'] += 0.3
        
        # Check PhishTank
        pt_result = self.check_phishing_url(url)
        if pt_result:
            results['sources'].append('phishtank')
            if pt_result.get('is_phishing'):
                results['threat_detected'] = True
                results['confidence_boost'] += 0.4
        
        # Check Google Safe Browsing
        gsb_result = self.check_google_safe_browsing(url)
        if gsb_result:
            results['sources'].append('google_safe_browsing')
            if gsb_result.get('is_unsafe'):
                results['threat_detected'] = True
                results['confidence_boost'] += 0.3
        
        return results


# Example usage in fraud_detector.py:
"""
from threat_intelligence import ThreatIntelligence

ti = ThreatIntelligence()

# In detect_url method:
if ti.enabled:
    threat_data = ti.enhanced_url_check(url)
    if threat_data['threat_detected']:
        confidence = min(confidence + threat_data['confidence_boost'], 1.0)
        is_fraud = True
"""


