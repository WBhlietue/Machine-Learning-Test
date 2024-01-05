from PIL import Image
import numpy as np

def GetPixels(url):
    image = Image.open(url)
    pixels = list(image.getdata())
    img = []
    num = 0
    width, height = image.size
    for i in range(height):
        w = []
        for j in range(width):
            w.append(pixels[num])
            num += 1
        img.append(w)
    return img

def ToPic(pixels):
    pixels = np.array(pixels, dtype=np.uint8)
    image = Image.fromarray(pixels)
    image.show()
