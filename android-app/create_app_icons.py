#!/usr/bin/env python3
"""
Generate Android launcher icons from wmm-logo.png
Requires: pip install Pillow
"""

from PIL import Image
import os

# Icon sizes for different densities
SIZES = {
    'mdpi': 48,
    'hdpi': 72,
    'xhdpi': 96,
    'xxhdpi': 144,
    'xxxhdpi': 192
}

# Paths
LOGO_PATH = 'app/src/main/assets/wmm-logo.png'
RES_PATH = 'app/src/main/res'

def create_icons():
    if not os.path.exists(LOGO_PATH):
        print(f"Error: Logo not found at {LOGO_PATH}")
        return
    
    # Load the original logo
    logo = Image.open(LOGO_PATH)
    print(f"Loaded logo: {logo.size}")
    
    # Create icons for each density
    for density, size in SIZES.items():
        folder = os.path.join(RES_PATH, f'mipmap-{density}')
        
        if not os.path.exists(folder):
            print(f"Warning: Folder not found: {folder}")
            continue
        
        # Resize the logo
        icon = logo.copy()
        icon.thumbnail((size, size), Image.Resampling.LANCZOS)
        
        # Create a square canvas with white background
        canvas = Image.new('RGB', (size, size), 'white')
        
        # Center the logo
        offset = ((size - icon.size[0]) // 2, (size - icon.size[1]) // 2)
        canvas.paste(icon, offset, icon if icon.mode == 'RGBA' else None)
        
        # Save both ic_launcher and ic_launcher_round
        launcher_path = os.path.join(folder, 'ic_launcher.png')
        launcher_round_path = os.path.join(folder, 'ic_launcher_round.png')
        
        canvas.save(launcher_path, 'PNG')
        canvas.save(launcher_round_path, 'PNG')
        
        print(f"Created {density}: {size}x{size}px")
    
    print("\n✅ All launcher icons created successfully!")
    print("Rebuild your APK to see the new icon.")

if __name__ == '__main__':
    create_icons()
