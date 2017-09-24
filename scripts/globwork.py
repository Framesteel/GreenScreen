import glob
from CustomGreenScreen import convertgreen
from PIL import Image
import moviepy.editor as mpy

list1 = glob.glob("../images/unconv/*")
size1 = len(list1)

avgx = 0
avgy = 0
gif1 = []

for i in range (0,(size1)):
    convertgreen (list1[i], i)
    img = Image.open("../images/conv/frame"+str(i)+".png")
    imgsize = img.size
    avgx = avgx + imgsize[0]
    avgy = avgy + imgsize[1]
    i+=1

for i in range (0,(size1)):
    img = Image.open("../images/conv/frame"+str(i)+".png")
    img = img.resize(((int)(avgx/4), (int)(avgy/4)))
    img.save("../images/conv/frame"+str(i)+".png")
    gif1.append("../images/conv/frame"+str(i)+".png")

gif_name = 'convertedGif'
fps = 6
file_list = glob.glob('../images/conv/*.png') # Get all the pngs in the current directory
file_list.sort
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('../images/gifs/{}.gif'.format(gif_name), fps=fps)
