# HiT-Logo-Importer
Python script to import a custom image into a save's logo in A Hat in Time.

## Dependencies ##
The script requires [python](https://www.python.org/downloads/) 3.6 or newer to run.

Additionally, you will need [opencv-python](https://pypi.org/project/opencv-python/) installed.

If you installed pip with the python installer or otherwise, you can run the following in a *command line* to install opencv.
```
py -m pip install opencv-python
```

## Running ##
Once python and opencv are installed, you run the script from a command line with arguments.

Format is `[-s (alias: --save)] SAVE_PATH [-i (alias: --image)] IMAGE_PATH`

For example, the command might look like the following on Windows with A Hat in Time on Steam.
```
py C:/Users/user/Downloads/HatLogo.py -s "C:\Program Files (x86)\Steam\steamapps\common\HatinTime\HatinTimeGame\SaveData\slot1.hat" -i C:/Users/user/Pictures/Logo.png
```

Where `Logo.png` is the image that you want to import to save file 1.

Most image formats will work to import from.

### Backups ###
Before importing a logo, the script will save a backup in the save's directory under the same backup format as the game. `slot<#>-Backup-<day>-<month>-<year>.bak`

If you lose the save file from running the script or you just want to undo the image import, you can revert to a backup by deleting everything after the slot and number, and replacing `.bak` with `.hat`.

For example, the name might go from `slot1-Backup-01-01-2000.bak` to `slot1.hat`.
