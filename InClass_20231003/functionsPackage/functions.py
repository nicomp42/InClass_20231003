# functions.py
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO

# functions here. Outside the entry point check.

# Will only run IF this is the entry point!
if __name__ == "__main__":
    print("I am in functions.py and I am NOT in a function")