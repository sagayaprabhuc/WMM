# Adding the WMM Logo to Your Android App

## Step 1: Save Your Logo
1. Save your logo image as `wmm-logo.png`
2. Recommended size: 800x600 pixels or similar aspect ratio
3. Format: PNG with transparent background (preferred)

## Step 2: Add Logo to Assets Folder
Copy `wmm-logo.png` to:
```
android-app/app/src/main/assets/wmm-logo.png
```

## Step 3: Rebuild the APK
```cmd
cd android-app
.\gradlew assembleDebug
```

## What's Been Fixed:

### ✅ Header Layout
- White background at top (no more green cutting off)
- Logo displays prominently
- Shop name and address below logo
- Proper spacing for Android notch/camera

### ✅ Invoice Template
- Logo appears in printed bills
- Professional layout with logo near shop name

### ✅ File Upload Support
- File chooser works for JSON imports
- Import medicines and customers from JSON files
- Proper Android file picker integration

### ✅ Android Compatibility
- Folder picker disabled (not supported in WebView)
- Data saves to app storage automatically
- All functions work in Android WebView

## Current Logo Location:
The logo file needs to be placed at:
`android-app/app/src/main/assets/wmm-logo.png`

If the logo file is missing, the app will still work but won't display the logo image.
