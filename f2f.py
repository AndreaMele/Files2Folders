# Author: Andrea Mele
# E-mail: andme44@gmial.com
# Websites: 
# http://www.github.com/AndreaMele
# http://www.artstation.com/AndreaMee
# Project: Files 2 Folders
"""
My scipt for dealing with Radarr Bulk Import

Takes all files, creates directories out of filenames.
Meant to be used after filebot or other pre-organized media files.

Handles duplicate filenames and clean up.
"""

import sys
import os
from pathlib import Path
import os.path
import shutil


def f2f():
    os.chdir(sys.path[0])
    filecounter = 0
    tempDir = os.path.join(sys.path[0] + "\\temp")
    tempDirList = []
    mainFileList = []
# --- Preventing a mess.
    if os.path.exists(tempDir):
        print("Temp Dir already exists, cannot proceed")
        print("Exiting")
        sys.exit()
# ----- Dealing with Temp Directory
    print("____________")
    if not os.path.exists(tempDir):
        print("... Temp Dir Created ...")
        os.mkdir(tempDir)
    else:
        for fn in os.listdir(tempDir):
            tempDirList.append(fn)  
# ----- Dealing with Temp Directory
# --------------------------------------
# ----- File dealings
    for root, dirs, files in os.walk(cDir, topdown=True):
        # exclude = tempDir
        exclude = tempDir
        dirs[:] = [d for d in dirs if d not in exclude]
        # if root  == tempDir:
        #     print("ding")
        #     continue
# --------- for file in files
        for filename in files:
            filecounter += 1
# Separate base from extension
            base, extension = os.path.splitext(filename)
# old default File
            oldFile = os.path.join(root, filename)
            oldFileFolder = os.path.join(root) + "\\"
# New name for Temp Folder
            newFile = os.path.join(tempDir, base, filename)
            print("   -    -  Processing File:  -    -    ")
            print("oldFile =>", oldFile)
            if filename == os.path.basename(sys.argv[0]): #Skip Script File
                print("Script file detected. Skipping...")
                continue
# If folder basedir/base does not exist... You don't want to create it?
            if not os.path.exists(os.path.join(tempDir, base + "\\")):
                try:
                    print("not found ... ", os.path.join(tempDir, base))
                    os.mkdir(os.path.join(tempDir, base))
                    print("Folder Created ... ", tempDir, base)
                    shutil.move(oldFile, newFile)
                    print("Relocated ... ", newFile)
                    continue    # Next filename
                except:
                    print("Error in try")
# folder exists, file does not
            elif not os.path.exists(newFile):  
                try:
                    print("Relocated ... ", newFile)
                    shutil.move(oldFile, newFile)
                except:
                    print("Error in elif")
# folder exists, file exists as well
            else:  
                vNum = 2
                while True:
                    newFile = os.path.join(tempDir, base, base + " - Ver " + str(vNum) + extension)
                    if not os.path.exists(newFile):
                        print(f"File : {filename} \nIN {tempDir} ... already exists")
                        try:
                            print(f"Renaming : {filename}\n To : {newFile}")
                            shutil.move(oldFile, newFile)
                            print(f"Copied : {oldFile}\nTo : {newFile}")
                            break 
                        except:
                            print("Error in Else")
                    vNum += 1
    # Clean up
    for root, dirs, files in os.walk(cDir, topdown=True):
        exclude = tempDir
        dirs[:] = [d for d in dirs if d not in exclude]
        print("_____ CLEAN UP ____")
        for dir in dirs:
            shutil.rmtree(dir)
            print("Removed : ", dir)
    # Moving files back to main directory
    files = os.listdir(tempDir)
    print(" Current Dir : ", cDir)
    print(" Temp Dir : ", tempDir)
    for f in files:
        shutil.copytree(tempDir, cDir, dirs_exist_ok=True)
        print(f)
    shutil.rmtree(tempDir)
    print("Removed : ", tempDir)
    print("\n\n\t\tall done.")

def main():
    f2f()

if __name__ == "__main__":
    cDir = os.getcwd()
    main()
