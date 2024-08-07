#Script will require python 3.6 or higher and opencv-python to run.
#Python: https://www.python.org/
#OpenCV: https://pypi.org/project/opencv-python/
#README: https://github.com/duckboycool/HiT-Logo-Importer/

import sys

#Checking for dependencies.
try:
    import os, argparse, cv2, datetime

except ModuleNotFoundError as module:
    #cv2 is not installed.
    if module.name == 'cv2':
        print("You need opencv (https://pypi.org/project/opencv-python/) to run this script.")
    
    else: #Should never be here (all other modules are standard lib), but will reraise error anyway.
        raise module
        
    sys.exit(-1)

#Parsing input image filepath and target save file.
parser = argparse.ArgumentParser(description="Used to replace the sketches/logos on your save's passport with an image of your choice.")

parser.add_argument('-s', '--save', type=str, help="The filepath to the save file you want to edit. Can be an absolute or relative path.", required=True)
parser.add_argument('-i', '--image', type=str, help="The filepath to the image you want to replace the current one with. Can be an absolute or relative path.", required=True)

paths = parser.parse_args()

if os.path.exists(paths.save):
    savedata = bytearray(open(paths.save, 'rb').read())

    #Creating backup of save file so if import fails, the file won't be lost.
    if savedata: #Don't write if savedata is empty.
        with open(f"{os.path.splitext(paths.save)[0]}-Backup-{datetime.date.today().strftime('%d-%m-%Y')}.bak", 'wb') as backup:
            backup.write(savedata)

    save = open(paths.save, 'wb')

else: #Save file does not exist at path.
    print(f'Did not find save file at "{paths.save}". Make sure the path is correct, and use absolute path if your working directory isn\'t in the SaveData folder.')
    sys.exit(-1)

image = cv2.imread(paths.image)

if image is None: #Image file does not exist at path.
    print(f'Did not find image at "{paths.image}". Make sure the path is correct, and use absolute path if your image isn\'t in your working directory.')
    sys.exit(-1)

image = cv2.resize(cv2.cvtColor(image, cv2.COLOR_BGR2RGBA), (512, 512), interpolation=cv2.INTER_NEAREST) #Converting to format and size stored in .hat files.

start = savedata.index(b'SketchingData') + 44 #Getting index of start of image data.
size = 4 * 512 ** 2

savedata[start:start + size] = bytearray(image) #Replace image data.

save.write(savedata)
save.close()
