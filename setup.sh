 echo "Building AppDir"
 rm -rf AppDir
 mkdir -p AppDir/usr/bin
 mkdir -p AppDir/usr/share/icons/hicolor/256x256/apps
 cp dist/krit-os-dashboard AppDir/usr/bin/
 cp assets/minato-namikaze-1920x1080-24353.png AppDir/usr/share/icons/hicolor/256x256/apps/krit-os.png
