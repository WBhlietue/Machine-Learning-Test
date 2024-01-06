import Picture.pictureToPixel as toPix
import Picture.convertToData as convert
import threading

def ShowImage(url):
    img = toPix.GetPixels(url)
    rgb = convert.SplitToRGB(img)
    rgb = convert.ToPooling(rgb)
    pic = convert.BlendRGB(rgb, [0, 1, 2])
    toPix.ToPic(pic)


def RunThread():
    threading.Thread(target=ShowImage, args=("./Picture/pictureData/cat/cat1.jpg", )).start()
    threading.Thread(target=ShowImage, args=("./Picture/pictureData/cat/cat2.jpg", )).start()
    threading.Thread(target=ShowImage, args=("./Picture/pictureData/cat/cat3.jpg", )).start()
    threading.Thread(target=ShowImage, args=("./Picture/pictureData/dog/dog1.jpg", )).start()
    threading.Thread(target=ShowImage, args=("./Picture/pictureData/dog/dog2.jpg", )).start()
    threading.Thread(target=ShowImage, args=("./Picture/pictureData/dog/dog3.jpg", )).start()

def RunSingle():
    ShowImage("./Picture/pictureData/cat/cat1.jpg")
    ShowImage("./Picture/pictureData/cat/cat2.jpg")
    ShowImage("./Picture/pictureData/cat/cat3.jpg")
    ShowImage("./Picture/pictureData/dog/dog1.jpg")
    ShowImage("./Picture/pictureData/dog/dog2.jpg")
    ShowImage("./Picture/pictureData/dog/dog3.jpg")

RunSingle()