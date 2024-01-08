import math
import numpy as np

def sigmoid(x):
    return (1 / (1+ np.exp(-x)))

def Z(a, w, b):
    return (a * w).sum(axis=1) + b

def GetYProd(x, w, b):
    z = Z(x, w, b)
    return sigmoid(z)

def CalcDistance(y, yProd):
    dis = (y - yProd) ** 2
    return dis.mean()

