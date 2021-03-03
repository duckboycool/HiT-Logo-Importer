#Script will require python 3.6 or higher and opencv-python to run.
#Python: https://www.python.org/
#OpenCV: https://pypi.org/project/opencv-python/
#README: https://github.com/duckboycool/HiT-Logo-Importer/

import sys

#Checking for dependencies.
try:
    import os, argparse, cv2

except ImportError:
    print("You need opencv (https://pypi.org/project/opencv-python/) to run this script.")
    sys.exit(-1)

#Parsing input image filepath and target save file.
parser = argparse.ArgumentParser(description="Used to replace the sketches/logos on your save's passport with an image of your choice.")

parser.add_argument('-save', type=str, help="The filepath to the save file you want to edit. Can be an absolute or relative path.")
parser.add_argument('-im', type=str, help="The filepath to the image you want to replace the current one with. Can be an absolute or relative path.")

paths = parser.parse_args()


if os.path.exists(paths.save):
    savedata = open(paths.save, 'rb').read()

    #Creating backup of save file so if import fails, the file won't be overwritten.
    with open(paths.save.replace('.hat', '.bak'), 'wb') as backup:
        backup.write(savedata)

    save = open(paths.save, 'wb')

else: #Save file does not exist at path.
    print(f'Did not find save file at "{paths.save}". Make sure the path is correct, and use absolute path if your working directory isn\'t in the SaveData folder.')
    sys.exit()

try:
    image = cv2.imread(paths.im)

except: #Image file does not exist at path.
    print(f'Did not find image at "{paths.im}". Make sure the path is correct, and use absolute path if your image isn\'t in your working directory.')
    sys.exit(-1)

image = cv2.resize(cv2.cvtColor(image, cv2.COLOR_BGR2RGBA), (512, 512), interpolation=cv2.INTER_NEAREST) #Converting to format and size stored in .hat files.

start = savedata.index(b'SketchingData') + 44 #Getting index of start of image data.
size = 512 ** 2

outsave = savedata[:start] #Save data before image start.

outsave += bytes(image)

outsave += savedata[start + 4 * size:] #Save data after image end.

save.write(outsave)
save.close()
