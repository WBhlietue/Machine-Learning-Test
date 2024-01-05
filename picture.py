import Picture.pictureToPixel as toPix
import Picture.convertToData as convert

url = "./Picture/pictureData/cat/cat4.jpg"

img = toPix.GetPixels(url)

print("split RGB start")
rgb = convert.SplitToRGB(img)
print("split RGB end")

print("convert start")
datas = convert.ToData(rgb)
print("convert end")
print("0")
rRow = convert.Compress(datas[0][0])
print("1")
gRow = convert.Compress(datas[1][0])
print("2")
bRow = convert.Compress(datas[2][0])
print("3")

r = convert.BlendRGB([rRow, gRow, bRow], [0, 0, 0])
g = convert.BlendRGB([rRow, gRow, bRow], [1, 1, 1])
b = convert.BlendRGB([rRow, gRow, bRow], [2, 2, 2])

toPix.ToPic(r)
toPix.ToPic(g)
toPix.ToPic(b)