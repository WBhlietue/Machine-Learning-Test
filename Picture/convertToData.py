import numpy as np
import threading
import multiprocessing

_min = 0
_max = 1
w1 = [[_max, _min, _min], [_min, _max, _min], [_min, _min, _max]]
w2 = [[_min, _min, _min], [_max, _max, _max], [_min, _min, _min]]


def SplitToRGB(img):
    r = []
    g = []
    b = []
    for j in range(len(img[0])):
        rRow = []
        gRow = []
        bRow = []
        for i in range(len(img)):
            rRow.append(img[i][j][0] / 255)
            gRow.append(img[i][j][1] / 255)
            bRow.append(img[i][j][2] / 255)
        r.append(rRow)
        g.append(gRow)
        b.append(bRow)
    return [r, g, b]


def BlendRGB(rgbs, mask=[0, 1, 2]):
    img = []
    for i in range(len(rgbs[0][0])):
        row = []
        for j in range(len(rgbs[0])):
            row.append(
                (
                    rgbs[mask[0]][j][i] * 255,
                    rgbs[mask[1]][j][i] * 255,
                    rgbs[mask[2]][j][i] * 255,
                )
            )
        img.append(row)
    return img

def PixelNormalize(pixels):
    list = []
    for i in range(len(pixels)):
        l = []
        for j in range(len(pixels[0])):
            l.append( pixels[i][j] / 255.0)
        list.append(l)
    list = vertical_flip(list)
    list = rotate_90_degrees(list)
    return list

def horizontal_flip(matrix):
    return [row[::-1] for row in matrix]

def vertical_flip(matrix):
    return matrix[::-1]

def rotate_90_degrees(matrix):
    rotated = list(zip(*matrix[::-1]))
    return [list(row) for row in rotated]

def ToDataBlend(img):
    dataR = np.zeros([len(img[0]) - 2, len(img[0][0]) - 2])
    dataG = np.zeros([len(img[0]) - 2, len(img[0][0]) - 2])
    dataB = np.zeros([len(img[0]) - 2, len(img[0][0]) - 2])
    full = len(img[0]) - 2

    def GetNum(channel):
        num1 = (
            w1[0][0] * img[channel][j][i]
            + w1[0][1] * img[channel][j + 1][i]
            + w1[0][2] * img[channel][j + 2][i]
            + w1[1][0] * img[channel][j][i + 1]
            + w1[1][1] * img[channel][j + 1][i + 1]
            + w1[1][2] * img[channel][j + 2][i + 1]
            + w1[2][0] * img[channel][j][i + 2]
            + w1[2][1] * img[channel][j + 1][i + 2]
            + w1[2][2] * img[channel][j + 2][i + 2]
        )
        num2 = (
            w2[0][0] * img[channel][j][i]
            + w2[0][1] * img[channel][j + 1][i]
            + w2[0][2] * img[channel][j + 2][i]
            + w2[1][0] * img[channel][j][i + 1]
            + w2[1][1] * img[channel][j + 1][i + 1]
            + w2[1][2] * img[channel][j + 2][i + 1]
            + w2[2][0] * img[channel][j][i + 2]
            + w2[2][1] * img[channel][j + 1][i + 2]
            + w2[2][2] * img[channel][j + 2][i + 2]
        )
        return num1, num2

    for j in range(len(img[0]) - 2):
        for i in range(len(img[0][0]) - 2):
            num1, num2 = GetNum(0)
            dataR[j][i] = max(num1, num2, 0)

            num1, num2 = GetNum(1)
            dataG[j][i] = max(num1, num2, 0)

            num1, num2 = GetNum(2)
            dataB[j][i] = max(num1, num2, 0)
    return [dataR, dataG, dataB]


def Compress(data):
    dataComp = np.zeros([int(len(data) / 2), int(len(data[0]) / 2)])
    full = int(len(data) / 2)
    for i in range(int(len(data) / 2)):
        for j in range(int(len(data[0]) / 2)):
            max = 0
            if max < data[i * 2][j * 2]:
                max = data[i * 2][j * 2]
            if max < data[i * 2 + 1][j * 2]:
                max = data[i * 2 + 1][j * 2]
            if max < data[i * 2][j * 2 + 1]:
                max = data[i * 2][j * 2 + 1]
            if max < data[i * 2 + 1][j * 2 + 1]:
                max = data[i * 2 + 1][j * 2 + 1]
            dataComp[i][j] = max
    return dataComp


def Comp(data):
    r = Compress(data[0])
    g = Compress(data[1])
    b = Compress(data[2])
    return [r, g, b]


def Resize(img, num):
    if max(len(img[0]), len(img[0][0])) > num:
        img = Comp(img)
        return Resize(img, num)
    res = [[[0] * num for _ in range(num)] for _ in range(3)]

    for j in range(len(img[0][0])):
        for i in range(len(img[0])):
            res[0][i][j] = img[0][i][j]
            res[1][i][j] = img[1][i][j]
            res[2][i][j] = img[2][i][j]
    return res

def ToPooling(img, size):
    data = ToDataBlend(img)
    data = Resize(data, size)
    return data


def ToLine(pixel):
    list = []
    for i in pixel:
        for j in i:
            list.append(j)
    return list