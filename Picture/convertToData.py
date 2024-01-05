import numpy as np

def SplitToRGB(img):
    r = []
    g = []
    b = []
    for i in img:
        rRow = []
        gRow = []
        bRow = []
        for j in i:
            rRow.append(j[0] / 255)
            gRow.append(j[1] / 255)
            bRow.append(j[2] / 255)
        r.append(rRow)
        g.append(gRow)
        b.append(bRow)
    return [r, g, b]

def BlendRGB(rgbs, mask = [0, 1, 2]):
    img = []
    for i in range(len(rgbs[0][0])):
        row = []
        for j in range(len(rgbs[0])):
            row.append((rgbs[mask[0]][j][i] * 255, rgbs[mask[1]][j][i] *255, rgbs[mask[2]][j][i] * 255))
        img.append(row)
    return img

def ToData(img):
    print("Start convert data")
    dataR1 = np.zeros([len(img[0][0])-2, len(img[0])-2])
    dataR2 = np.zeros([len(img[0][0])-2, len(img[0])-2])
    dataG1 = np.zeros([len(img[0][0])-2, len(img[0])-2])
    dataG2 = np.zeros([len(img[0][0])-2, len(img[0])-2])
    dataB1 = np.zeros([len(img[0][0])-2, len(img[0])-2])
    dataB2 = np.zeros([len(img[0][0])-2, len(img[0])-2])
    full = (len(img[0][0]) - 2)
    for i in range(len(img[0][0]) - 2):
        print(f"progress {(i+1)/full*100: .2f}%", end="\r")
        for j in range(len(img[0]) - 2):
            num1 = 0 * img[0][j][i] + 1 * img[0][j+1][i] + 0 * img[0][j+2][i] +  0 * img[0][j][i+1] + 1 * img[0][j+1][i+1] + 0 * img[0][j+2][i+1] +  0 * img[0][j][i+2] + 1 * img[0][j+1][i+2] + 0 * img[0][j+2][i+2] 
            num2 = 0 * img[0][j][i] + 0 * img[0][j+1][i] + 0 * img[0][j+2][i] +  1 * img[0][j][i+1] + 1 * img[0][j+1][i+1] + 1 * img[0][j+2][i+1] +  0 * img[0][j][i+2] + 0 * img[0][j+1][i+2] + 0 * img[0][j+2][i+2]
            dataR1[i][j] = num1
            dataR2[i][j] = num2 

            num1 = 0 * img[1][j][i] + 1 * img[1][j+1][i] + 0 * img[1][j+2][i] +  0 * img[1][j][i+1] + 1 * img[1][j+1][i+1] + 0 * img[1][j+2][i+1] +  0 * img[1][j][i+2] + 1 * img[1][j+1][i+2] + 0 * img[1][j+2][i+2] 
            num2 = 0 * img[1][j][i] + 0 * img[1][j+1][i] + 0 * img[1][j+2][i] +  1 * img[1][j][i+1] + 1 * img[1][j+1][i+1] + 1 * img[1][j+2][i+1] +  0 * img[1][j][i+2] + 0 * img[1][j+1][i+2] + 0 * img[1][j+2][i+2]
            dataG1[i][j] = num1
            dataG2[i][j] = num2 

            num1 = 0 * img[2][j][i] + 1 * img[2][j+1][i] + 0 * img[2][j+2][i] +  0 * img[2][j][i+1] + 1 * img[2][j+1][i+1] + 0 * img[2][j+2][i+1] +  0 * img[2][j][i+2] + 1 * img[2][j+1][i+2] + 0 * img[2][j+2][i+2] 
            num2 = 0 * img[2][j][i] + 0 * img[2][j+1][i] + 0 * img[2][j+2][i] +  1 * img[2][j][i+1] + 1 * img[2][j+1][i+1] + 1 * img[2][j+2][i+1] +  0 * img[2][j][i+2] + 0 * img[2][j+1][i+2] + 0 * img[2][j+2][i+2]
            dataB1[i][j] = num1
            dataB2[i][j] = num2
    print("Convert Complete") 
    return [[dataR1, dataR2], [dataG1, dataG2], [dataB1, dataB2]]

def Compress(data):
    print("compressing")
    dataComp = np.zeros([int(len(data) / 2), int(len(data[0]) / 2)])
    full = int(len(data) / 2)
    for i in range(int(len(data) / 2)):
        print(f"progress {(i+1)/full*100: .2f}%", end="\r")
        for j in range(int(len(data[0]) / 2)):
            max = 0
            if(max < data[i*2][j*2]):
                max = data[i*2][j*2]
            if(max < data[i*2+1][j*2]):
                max = data[i*2+1][j*2]
            if(max < data[i*2][j*2+1]):
                max = data[i*2][j*2+1]
            if(max < data[i*2+1][j*2+1]):
                max = data[i*2+1][j*2+1]
            dataComp[i][j] = max 
    print("compress over")
    return dataComp
            
