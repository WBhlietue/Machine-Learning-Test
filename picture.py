import Picture.pictureToPixel as toPix
import Picture.convertToData as convert

def ShowImage(url):
    img = toPix.GetPixels(url)
    rgb = convert.SplitToRGB(img)
    rgb = convert.ToPooling(rgb)
    pic = convert.BlendRGB(rgb, [0, 1, 2])
    toPix.ToPic(pic)


ShowImage("./Picture/pictureData/cat/cat1.jpg")