#!/usr/bin/env python

import re
import os
import pdb
import sys

def GetFileName():
    dirname = os.path.dirname(os.path.abspath(__file__))
    base, folname = os.path.split(dirname)
    return folname + '.tex'

def GenerateBB(filename):
    for line in open(filename, 'r', encoding='utf-8'):
        img = GetImages(line)
        if img != None:
            Exec('ebb ' + img)

def GetImages(line):
    ext = '(png|jpg|gif|bmp)'
    p = re.compile('([a-zA-Z0-9]+)\.' + ext)
    m = p.search(line)
    if m != None:
        return m.group(0)

def GeneratePDF(filename):
    base, ext = os.path.splitext(filename)
    Exec('platex ' + base + '.tex')
    Exec('dvipdfmx ' + base + '.dvi')

def Exec(cmd):
    os.system(cmd)

#main
argvs = sys.argv
argc = len(argvs)
if argc == 1:
     filename = GetFileNames()
elif argc == 2:
    filename = argvs[1]
else:
    print("Usage: # python {0} [filename]".format(argvs[0]))
    quit()
GenerateBB(filename)
GeneratePDF(filename)

