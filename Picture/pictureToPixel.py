from PIL import Image
import numpy as np
import threading 

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

def ShowImage(pixels):
    image = Image.fromarray(pixels)
    image.show()

def ToPic(pixels):
    pixels = np.array(pixels, dtype=np.uint8)
    tr = threading.Thread(target=ShowImage, args=(pixels, ))
    tr.start()
