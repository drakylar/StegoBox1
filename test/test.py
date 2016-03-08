import numpy
from PIL import Image
from PIL import ImageChops
im_and = ImageChops.lighter

im = Image.open('/Users/iljashaposhnikov/Desktop/python/Steganogaphy/test/image.jpg')


pix = im.load()
for x in range(100):
    for y in range(100):
        pix[x,y]=(0,0,0)
im.show()