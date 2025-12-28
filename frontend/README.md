# NEURA Web Frontend

A simple web-based interface to test and visualize the NEURA fraud detection API.

## How to Use

1. **Make sure the backend is running:**
   ```bash
   cd backend
   python main.py
   ```

2. **Open the frontend:**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     # Python 3
     python -m http.server 8080
     
     # Then open: http://localhost:8080
     ```

3. **Test the API:**
   - Select a tab (SMS, Call, Email, URL)
   - Enter the data to scan
   - Click "Scan" button
   - View the results with color-coded risk levels

## Features

- ✅ Real-time API connection status
- ✅ Four scan types: SMS, Call, Email, URL
- ✅ Visual risk indicators (Green/Yellow/Red)
- ✅ Scan history
- ✅ Responsive design
- ✅ No backend required - pure HTML/CSS/JavaScript

## API Connection

The frontend connects to `http://localhost:8000` by default.

To change the API URL, edit the `API_BASE` variable in `index.html`:
```javascript
const API_BASE = 'http://localhost:8000';
```

## Troubleshooting

**"Disconnected" status:**
- Make sure the backend server is running
- Check if it's on port 8000
- Verify CORS is enabled in the backend

**CORS errors:**
- The backend already has CORS enabled
- If issues persist, check browser console for errors


