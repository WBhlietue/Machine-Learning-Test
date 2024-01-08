from keras.datasets import mnist
import Picture.convertToData as convert
import Picture.pictureToPixel as toPix
import matplotlib.pyplot as plt
import Picture.calculateW as calc
import numpy as np
from keras.utils import to_categorical


def ReadData(num):
    (trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()
    trainLabel = to_categorical(trainLabel)
    def GetArray(num):
        pixel = trainImage[num]
        pixel = convert.PixelNormalize(pixel)
        pixel = convert.ToPooling([pixel, pixel, pixel], 26)
        line = np.array(convert.ToLine(pixel[0]))
        pixel = convert.BlendRGB(pixel, [0, 1, 2])
        tr = toPix.ToPic(pixel)
        tr.join()
        return line
    list = []
    y = []
    for i in range(num):
        if(i % 100 == 0):
            print(i)
        list.append(GetArray(i))
        y.append(trainLabel[i])
    return (list, y)




# data = ReadData(100)
def GetRealY(index):
    list = []
    for i in data[1]:
        list.append(i[index])
    list = np.array(list)
    return list


# x = np.array(data[0])
# z = calc.GetYProd(x, np.array([1] * len(data[0][0])), 1)


# yReal = GetRealY(0)

# print(x)
# print(np.array([1] * len(data[0][0])))

def GradientNew(x, y, w, b):
  print(x)
  print(w)
  yCalc = calc.GetYProd(x, w, b)
  bG = (yCalc - y).mean()
  wG = np.zeros(x.shape[1])
  for i in range(x.shape[1]):
    wG[i] = (x[:, i] * (yCalc - y)).mean()
  return wG, bG

def GradientRunNew(x, y, maxNum, learningRate):
  initW = np.array([0.0] * len(data[0][0]))
  initB = 0
  costBack = -1
  for i in range(maxNum):
    stepW, stepB = GradientNew(x, y, np.array([1] * len(data[0][0])), initB)
    initW -= learningRate * stepW
    initB -= learningRate * stepB
    yCalc = calc.GetYProd(x, initW, initB)
    cost = calc.CalcDistance(y, yCalc)
    if(i % 10 == 0):
      print(f"Running, {i/maxNum * 100:.2f}%")
    if(costBack < 0 or costBack > cost):
      costBack = cost
    elif(costBack < cost):
      print("over")
      return initW + learningRate * stepW, initB + learningRate * stepB

  return initW, initB

# GradientRunNew(x, yReal, 1000, 0.01)

ReadData(1000)