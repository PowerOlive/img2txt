#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage: img2txt.py <imgfile> [--maxLen=<maxLen>] [--fontSize=<fontSize>] [--color]

"""

from docopt import docopt

dct = docopt(__doc__)

imgname = dct['<imgfile>']

maxLen = dct['--maxLen']

clr = dct['--color']

fontSize = dct['--fontSize']

try:
    maxLen = float(maxLen)
except:
    maxLen = 100.0   # default maxlen: 100px

try:
    fontSize = int(fontSize)
except:
    fontSize = 7


import Image

try:
    img = Image.open(imgname)
except IOError:
    exit("File not found: " + imgname)

# resize to: the max of the img is maxLen

width, height = img.size

rate = maxLen / max(width, height)

width = int(rate * width)  # cast to int

height = int(rate * height)

img = img.resize((width, height))

# img = img.convert('L')

# get pixels
pixel = img.load()

# grayscale
color = "MNHQ$OC?7>!:-;. "

string = ""

for h in xrange(height):  # first go through the height,  otherwise will roate
    for w in xrange(width):
        rgb = pixel[w, h]
        if clr:
            string += "<span style=\"color:rgb" + str(rgb) + \
                ";\">▇</span>"
        else:
            string += color[int(sum(rgb) / 3.0 / 256.0 * 16)]
    string += "\n"

# wrappe with html

style = """
<!-- Generated by https://github.com/hit9/img2txt -->
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <style>
        .imgtxt{
            -webkit-text-size-adjust:none;
            font-size:""" + str(fontSize) + """px;
            line-height:1;
        }
    </style>
    </head>
"""

html = style + "<body><pre class=\"imgtxt\">" + string + "</pre></body><html>"

print html
