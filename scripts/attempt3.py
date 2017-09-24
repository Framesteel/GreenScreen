from SimpleCV import *
from PIL import Image

img = Image.open("../images/unconv/demo1.jpg")
img = img.convert("RGBA")
datas = img.getdata()
img.show()

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
img.show()
time.sleep(2)

img2 = img.resize(size)
img2.save("../images/conv/demo1.png")
img2.show()
