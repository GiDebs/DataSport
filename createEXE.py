# Create an .exe file that anyone can use
# The .exe file is inside dist folder
import pathlib
import PyInstaller.__main__

PyInstaller.__main__.run([
    'import.py',               # Put the name of the code here (must be in the same directory of this script)
    '--onefile',               # Create only the .exe file in the 
    '--windowed'
])


# Zip the dist folder
import shutil
shutil.make_archive('AtleticaLevante', 'zip', 'dist')

