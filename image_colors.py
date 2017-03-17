#!/usr/bin/env python3
import argparse
import logging
import os
import re
from math import ceil
from random import randint, random, seed, randrange
from urllib2 import urlopen
#from urllib.request import urlopen

from PIL import Image


def get_cli_args():
    """
    Parses command line arguments.
    :return: An object whose fields are the command line arguments.
    """
    parser = argparse.ArgumentParser(description='A tool for pixel-sorting images')
    parser.add_argument("infile", help="The input image")
    ##parser.add_argument("-o", "--outfile", required=True, help="The output image")
    args = parser.parse_args()
    return args


def load_image(args):
	# load image
  if re.match(r"https?://", args.infile):
    response = urlopen(args.infile)
    #img_size = int(response.getheader("Content-Length"))
    img = Image.open(response)
  else:
    img = Image.open(args.infile)

  gif = False
  if img.tile[0][0] == "gif":
    gif = True
  # converting modes in gifs seems to remove all frames but the first
  if img.mode != "RGB" and not gif:
    img = img.convert(mode="RGB")

  return img

def save_image(pixels, outfile, img):
	 # write output image
  img_out = Image.new(img.mode, (5,1))
  img_out.putdata(pixels)
  img_out.save(outfile)

def main():
	args = get_cli_args()

	img = load_image(args)
	pix = img.load()
	width = img.size[0]
	height = img.size[1]

	print pix[0,0]

	colors = []
	for c in range(5):
		rx = randrange(0,width) 
		ry = randrange(0,height) 
		#for i in range(50):
		colors.append(pix[rx,ry])
  
	outfile = "output.png"

	save_image(colors, outfile, img)
 
# static/img/unsplash_forest.jpeg

if __name__ == '__main__':
	main()










