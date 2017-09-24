from SimpleCV import *
from PIL import Image
import numpy as np

premask = Image.open("../images/unconv/run4.jpg")
prergb = premask.load()
presize = premask.size
print premask.size
print prergb[0,0]

x = presize[0]
y = presize[1]

list1= np.zeros((x,y,3), dtype=np.uint8)
newData = (x,y)

print x
print y

for i in range(0,x):
    for j in range(0,y):
        value = prergb[i,j]
        if (value[1] > 150) and (value[0] < 210) and (value[2] < 150):
            newData[i,j].append((255,255,255, 0))
            #list1[i,j] = [0,0,0]
        #else:
            #newData.append()
            #list1[i,j] = value
        j+=1
    i+=1

size = 200, 100
postimg = Image.fromarray(list1, 'RGB')
postimg2 = postimg.resize(size, Image.ANTIALIAS)
postimg2.show()
postimg2.save("../images/conv/run4.jpg")
