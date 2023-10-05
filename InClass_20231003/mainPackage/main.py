# main.py
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO
from functionsPackage.functions import *

# Check to see if this was our entry point:
# in other words, was this tab active when we clicked "Run"
if __name__ == "__main__":
    # all our code goes here
    # open an image file. The default path is where this python module is
    # we need to build a path so this code
    # can find our jpg file!
    # This is an absolute path: specific to my system!
    #im = Image.open(r"C:\Users\nicholdw\OneDrive - University of Cincinnati\Documents\Google Drive\Fall 2023 IS4010-001 Python\Fall 2023 Eclipse Workspace\InClass_20231003\imageArchivePackage\ImageArchive\SiriusAndViolet.jpg")
    im = Image.open(r"..\imageArchivePackage\ImageArchive\SiriusAndViolet.jpg")
    print(im.width, im.height, im.mode, im.format)  # Display some info about the image
