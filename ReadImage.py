import Picture.pictureToPixel as toPix 
import Picture.convertToData as convert

def ShowImage(url):
    img = toPix.GetPixels(url)
    rgb = convert.SplitToRGB(img)
    rgb = convert.ToPooling(rgb, 28)
    line = convert.ToLine(rgb[0])
    return line
    pic = convert.BlendRGB(rgb, [0, 1, 2])
    tr = toPix.ToPic(pic)
    tr.join()

ShowImage("./2.png")