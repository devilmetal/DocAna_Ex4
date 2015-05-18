from PIL import Image
import math
import numpy as np
import collections
from matplotlib import pyplot as plt
import sys
import os
import random
import operator
import pickle

BLACK = 0.0
WHITE = 1.0


# ---- FEATURES EXTRACTION /begin ---- #
def extract(fname):
    im = Image.open(fname).convert('L')
    pixels = im.load()
    width, height = im.size
    img = []
    for i in range(width):
        line = []
        for j in range(height):
            if pixels[i,j] > 127:
                cpixel = WHITE
            else:
                cpixel = BLACK
            line.append(cpixel)
        img.append(line)
    return img
# ---- FEATURES EXTRACTION /end ---- #



# ------------------------- M A I N -------------------------#

# ws_path = "images/train/"
# # FILE TO PRINT STUFF IN
# file_output =  open('train_pv.txt','wb')
# file_output.write('')
# file_output.close()
# file_output = open('train_pv.txt','ab')

ws_path = "images/train/"
# FILE TO PRINT STUFF IN
file_output =  open('train_pv.txt','wb')
file_output.write('')
file_output.close()
file_output = open('train_pv.txt','ab')

for path, subdirs, files in os.walk(ws_path):
    #checking files
    for file in files:
        #NAME STUFF
        fname = ws_path+file
        label = file.split('-')[1][-1]

        #COMPUTE STUFF
        feature = []
        feature.append(str(label))
        pv = extract(fname)
        width, height = len(pv), len(pv[0])

        for y in range(height):
            for x in range(width):
                feature.append(str(pv[x][y]))


        # PRINT STUFF
        sep = ','
        stuff =  sep.join(feature) + '\n'
        print 'file '+fname+' encoded'
        file_output.write(stuff)
