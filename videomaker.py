from ASCIIImage.sprite import sprite
from ASCIIImage.manipulate import *

length = 20
frames = 0
data = ""

def display(content,time):
	global length
	global data
	global frames
	content = setSize(str(content),0,length)
	content = crop(str(content),60,length)
	data += content + str(time)+"\n"
	frames +=1







print("{:03d}y{:06d}".format(length,frames)+data)

