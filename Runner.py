import TTest as main
import Picture.calculateW as calc
from keras.datasets import mnist
import Picture.convertToData as convert
import Picture.pictureToPixel as toPix
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import to_categorical

data = main.ReadData(50000)

def GetRealY(index):
    list = []
    for i in data[1]:
        list.append(i[index])
    list = np.array(list)
    return list


x = np.array(data[0])
z = calc.GetYProd(np.array(data[0]), np.array([1] * len(data[0][0])), 1)

(trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()
def GradientNew(x, y, w, b):
  yCalc = calc.GetYProd(x, w, b)
  bG = (yCalc - y).mean()
  wG = np.zeros(x.shape[1])
  for i in range(x.shape[1]):
    wG[i] = (x[:, i] * (yCalc - y)).mean()
  return wG, bG

def GradientRunNew(x, maxNum, learningRateNum, col):
  learningRate = 1
  y = GetRealY(col)
  initW = np.array([0.0] * len(data[0][0]))
  initB = 0
  costBack = -1
  for i in range(maxNum):
    stepW, stepB = GradientNew(x, y, np.array([1] * len(data[0][0])), initB)
    initW -= learningRate * stepW
    initB -= learningRate * stepB
    yCalc = calc.GetYProd(x, initW, initB)
    cost = calc.CalcDistance(y, yCalc)
    if(i % 100 == 0):
      print(f"Running, {i/maxNum * 100:.2f}%, cost: {cost}")
    if(costBack < 0 or costBack > cost):
      costBack = cost
    elif(costBack <= cost):
      print("reverse")
      print(f"Running, {i/maxNum * 100:.2f}%, cost: {cost}")
      learningRate /= 10
      learningRateNum -= 1
      if(learningRateNum == 0):
        print(cost)
        print("over")
        return initW , initB 

  return initW, initB
def GetCurrentImage(num, index):
    # (trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()
    testLabels = to_categorical(trainLabel)
    pixel = trainImage[num]
    pixel = convert.PixelNormalize(pixel)
    pixel = convert.ToPooling([pixel, pixel, pixel], 28)
    line = np.array(convert.ToLine(pixel[0]))
    return pixel, line, testLabels[num][index]

def CheckAcc(line, ans, w, b):
    x = (line * w).sum() + b
    return x 


w = []
b = []
for i in range(10):
    print(f"run {i}")
    w1, b1 = GradientRunNew(x, 10000, 20, i)
    w.append(np.array(w1))
    b.append(np.array(b1))


w = np.array(w)
wNew = w.mean(axis=0)
b = np.array(b)
bNew = b.mean()
(trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()
trainLabel
numTotal = 0
numCorrect = 0
for i in range(52000, 53000):
    list = []
    for j in range(10):
        pixel, line, ans = GetCurrentImage(i, j)
        per = (int)(CheckAcc(line, ans, w[j], b[j])*100)/100
        list.append(per)
    sorted_indices = np.argsort(list)
    if(trainLabel[i] == sorted_indices[-1]):
        numCorrect += 1
    numTotal += 1
    print(f"Num of: {numTotal}, Answer is {trainLabel[i]} result is {sorted_indices[-1]}, accuracy: {numCorrect / numTotal * 100:.2f}%")

print(f"Final accuracy is {numCorrect / numTotal * 100:.2f}%")