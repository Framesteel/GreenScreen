from SimpleCV import *
from PIL import Image

def convertgreen (a,b):
    img = Image.open(a)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if (item[0] < 200 and item[1] > 150 and item[2] < 115) or (item[0] > 180 and item[1] > 180 and item[2] > 180):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    presize = img.size
    x = (int)(presize[0]*.08)
    y = (int)(presize[1]*.08)
    size = (x,y)
    img.putdata(newData)

    img2 = img.resize(size)
    str1 = "../images/conv/frame"
    str1 = str1 + str(b) + ".png"
    img2.save(str1)
    return;
