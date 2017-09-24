'''
This program takes a person standing in front of a green screen
and then removes the background and inserts a new one
'''
print __doc__

from SimpleCV import *

sleep_time = 2 #the amount of time to show each image for

#Load and show the greenscreen image
print "Showing Greenscreen image"
greenscreen = Image("../images/unconv/newimg.jpg")


#Create the mask to apply and show the mask
print "Showing Masked Image"
mask = greenscreen.hueDistance(color=Color.GREEN).binarize(20)

#Combine the mask and other images to get the final result
print "Showing final image"
result = (greenscreen - mask)
result.show()
time.sleep(4)
