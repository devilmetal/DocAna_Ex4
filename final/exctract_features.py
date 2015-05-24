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

BLACK = 0
WHITE = 255

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



# ---- FEATURES EXTRACTION /begin ---- #
# Projection Profiling Columns
def pp_col(fname):
    img = extract(fname)
    width, height = len(img), len(img[0])
    pp = []
    # for each column count the number of black pixels
    for i in range(width):
        sum_black = 0
        for j in range(height):
            if img[i][j] == BLACK:
                sum_black += 1
        sum_black = sum_black/float(height)
        pp.append(sum_black)

    # normalize
    norm_pp = normalize(pp)
    return norm_pp


# Projection Profiling Columns Transition B/W
def pp_col_transition(fname):
    img = extract(fname)
    width, height = len(img), len(img[0])
    pp = []
    # for each column count the number of black pixels
    for i in range(width):
        transitions = 0
        white = True
        for j in range(height):
            if white:
                if img[i][j] == BLACK:
                    transitions += 1
                    white = False
            else:
                if img[i][j] == WHITE:
                    transitions += 1
                    white = False

        pp.append(transitions)
    # normalize
    norm_pp = normalize(pp)
    return norm_pp


# Upper Profile
def up(fname):
    img = extract(fname)
    width, height = len(img), len(img[0])
    up = []
    for i in range(width):
        sum_white = 0
        j=0
        while j < height and img[i][j] == WHITE:
            j+=1
            sum_white += 1
        if sum_white == height:
            sum_white = int(height/2)
        up.append(sum_white)
    # normalize
    norm_up = normalize(up)
    return norm_up

def lp(fname):
    img = extract(fname)
    width, height = len(img), len(img[0])
    lp = []
    for i in range(width):
        sum_white = 0
        j=height-1
        while j >= 0 and img[i][j] == WHITE:
            j-=1
            sum_white += 1
        if sum_white == height:
            sum_white = int(height/2)
        lp.append(sum_white)
    # normalize
    norm_up = normalize(lp)
    return norm_up


def normalize(x):
    ma = max(x)
    mi = min(x)
    if ma == mi:
        mi = 0
    for i in range(len(x)):
        x[i] = (x[i]-mi)/float(ma-mi)

    return x

# ---- FEATURES EXTRACTION /end ---- #



# ------------------------- M A I N -------------------------#

# Keywords
ws_path = "images/train/"
# FILE TO PRINT STUFF IN
file_output =  open('train.txt','wb')
file_output.write('')
file_output.close()
file_output = open('train.txt','ab')

for path, subdirs, files in os.walk(ws_path):
    #checking files
    for file in files:
        #NAME STUFF
        fname = ws_path+file
        label = file.split('-')[1][-1]

        #COMPUTE STUFF
        pp = pp_col(fname)
        pp_trans = pp_col_transition(fname)
        upperp = up(fname)
        lowerp = lp(fname)

        # PRINT STUFF
        pp_for_print = (str(w) for w in pp)
        pp_trans_for_print = (str(w) for w in pp_trans)
        upperp_for_print = (str(w) for w in upperp)
        lowerp_for_print = (str(w) for w in lowerp)
        stuff =  label+', '+', '.join(pp_for_print)+', '+', '.join(pp_trans_for_print)+', '+', '.join(upperp_for_print)+', '+', '.join(lowerp_for_print)+'\n'
        print 'file '+fname+' encoded'
        file_output.write(stuff)
