# This program will open a random image from a specified folder

import random, os
from PIL import Image
imgdir = "enter path to image folder here"
imgfile = random.choice(os.listdir(imgdir))
impath = imgdir + str(imgfile)
print(impath)
im = Image.open(impath)
im.show()

