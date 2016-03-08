from PIL import Image, ImageTk,ImageOps,ImageFilter
def rotate90(image):
    return image.transpose(Image.ROTATE_90)

def rotate180(image):
    return image.transpose(Image.ROTATE_180)

def sepia(image):
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            c = (r+g+b)//3
            pixels[x,y] = (c,c,c)
    return image

def whitePixels(image):
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            if not r==g==b:
                pixels[x,y] = (0,0,0)
    return image

def invert(image):

    return ImageOps.invert(image)

def colorShow(image,plane):
    #'0:10:22'
    print('plane',plane)
    plane = plane.replace('::',':')
    if plane[0]==':':plane=plane[1:]
    if plane[len(plane)-1]==':': plane = plane[:len(plane)-1]
    plane = plane.split(':')
    #[0,10,22]
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            stay = 0
            for color in plane:
                if int(color)<=7:
                    if 32*int(color)<r<=32*(int(color)+1):
                        stay = 1
                elif int(color)<=15:
                    if 32*(int(color)-8)<g<=32*(int(color)-7):
                        stay=1
                elif int(color)<=23:
                    if 32*(int(color)-16)<b<=32*(int(color)-15):
                        stay=1
            if not stay: pixels[x,y] = (255,255,255)
            else: pixels[x,y] = (0,0,0)

    return image

def edge(image):
    return image.filter(ImageFilter.FIND_EDGES)

def contour(image):
    return image.filter(ImageFilter.CONTOUR)