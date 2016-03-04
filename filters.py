from PIL import Image, ImageTk
def rotate90(image):
    return image.transpose(Image.ROTATE_90)

def rotate180(image):
    return image.transpose(Image.ROTATE_180)

def sepia(image):
    pixels = image.convert('RGB')
    width, height = image.size
    r, g, b = image.getpixel((1, 1))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            c = (r+g+b)//3
            image.putpixel( (x,y), (c,c,c))
    return image

def whitePixels(image):
    pixels = image.convert('RGB')
    width, height = image.size
    r, g, b = image.getpixel((1, 1))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if not r==g==b:
                image.putpixel( (x,y), (0,0,0))
    return image