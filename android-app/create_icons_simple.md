# Create App Icons - Simple Method

## Option 1: Online Tool (Easiest - No Installation)

1. **Go to:** https://icon.kitchen/
2. **Upload** your `wmm-logo.png`
3. **Customize:**
   - Select "Image" source type
   - Adjust padding if needed
   - Choose "Legacy" icon format
4. **Download** the icon pack
5. **Extract** the zip file
6. **Copy** all folders from the zip to:
   ```
   android-app/app/src/main/res/
   ```
   Replace the existing mipmap folders

## Option 2: Manual with Paint/Photo Editor

For each folder, create these sizes:

### mdpi (48x48px)
- Location: `app/src/main/res/mipmap-mdpi/`
- Files: `ic_launcher.png`, `ic_launcher_round.png`

### hdpi (72x72px)
- Location: `app/src/main/res/mipmap-hdpi/`
- Files: `ic_launcher.png`, `ic_launcher_round.png`

### xhdpi (96x96px)
- Location: `app/src/main/res/mipmap-xhdpi/`
- Files: `ic_launcher.png`, `ic_launcher_round.png`

### xxhdpi (144x144px)
- Location: `app/src/main/res/mipmap-xxhdpi/`
- Files: `ic_launcher.png`, `ic_launcher_round.png`

### xxxhdpi (192x192px)
- Location: `app/src/main/res/mipmap-xxxhdpi/`
- Files: `ic_launcher.png`, `ic_launcher_round.png`

## Option 3: Use Python Script

If you have Python installed:

```cmd
cd android-app
pip install Pillow
python create_app_icons.py
```

## After Creating Icons

Rebuild the APK:
```cmd
cd android-app
.\gradlew assembleDebug
```

The new app icon will appear on your phone's home screen!
