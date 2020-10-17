
# Files2Folders

**Author:** Andrea Mele

**E-mail:** andme44@gmial.com

**Websites:**
> http://www.github.com/AndreaMele

> http://www.artstation.com/AndreaMele


*Takes all files (in all sub/directories), creates directories out of filenames. Handles duplicate filenames and clean up.*


**Files 2 Folder Features**
- [x] Takes all files and puts them into folders using the files' name.
- [x] Handles same filenames.
- [x] Sort directories.
- [x] Cleans up previous files.
- [x] Logs Changes to files saved in \Logs\ folder.

## When to Use

Lets say you've used filebot on 100's of files to rename the files, but have forgten to name the folders in the process, or your just happy with the file names and want to create folders using the filename, this will do that.

Great for further organizing assets that need folder separation. For example: JPEG's that will need iterations.

Many uses, be creative!

## How To Use

Prerequisites:
[Python 3.8+](https://www.python.org/downloads/)

**Steps:**

Place script in root directory of any files. If you want to sort files in your movies folder located at **D:\Movies** place the script in Movies folder so it looks like: **D:\Movies\f2f.py**

Click **Start** > **Run** , Type: 

    Cmd.exe

Navigate to script location, Type:

    cd /d D:\Movies\

Start the script, Type:

    f2f.py

Example of Results below:

![Example of Output](https://raw.githubusercontent.com/AndreaMele/Files2Folders/master/example.png)
