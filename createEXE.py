# Create an .exe file that anyone can use
# The .exe file is inside dist folder
import shutil
import os
import PyInstaller.__main__

PyInstaller.__main__.run([
    'import.py',               # Put the name of the code here (must be in the same directory of this script)
    '--onefile',               # Create only the .exe file in the 
    '--windowed'
])
# Add the necassary folder in dist 
directory = "Origini"
parent_dir = r"C:\Users\Giulio\Documents\GitHub\DataSport\dist"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
# Zip the dist folder
import shutil
shutil.make_archive('AtleticaLevante', 'zip', 'dist')

