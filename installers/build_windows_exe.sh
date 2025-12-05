#!/bin/bash
# Windows Executable Builder for KRIT OS
# Builds a standalone .exe using PyInstaller

echo "======================================"
echo "KRIT OS - Windows Executable Builder"
echo "======================================"
echo ""

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
fi

# Navigate to project root
cd ..

echo "Building Windows executable..."
echo ""

# Build with PyInstaller
pyinstaller --name="KRIT-OS" \
    --onefile \
    --windowed \
    --icon="assets/logo.ico" \
    --add-data="config.json;." \
    --add-data="krit;krit" \
    --add-data="assets;assets" \
    --hidden-import="pyttsx3.drivers" \
    --hidden-import="pyttsx3.drivers.sapi5" \
    --hidden-import="speech_recognition" \
    --hidden-import="psutil" \
    --hidden-import="tkinter" \
    --collect-all="pocketsphinx" \
    --collect-all="speech_recognition" \
    main.py

echo ""
echo "Build complete!"
echo "Executable location: dist/KRIT-OS.exe"
echo ""
echo "To create installer, run:"
echo "  makensis installer_script.nsi"
echo ""