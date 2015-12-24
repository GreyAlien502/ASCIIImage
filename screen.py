from ASCIIImage.asciiimage import asciiimage
from ASCIIImage.manipulate import *
from ASCIIImage.asciivideo import asciivideo, frame
from ASCIIImage.sprite     import sprite
from math import floor

class screen:
	def __init__(self,initial_sprite,length=None,width=None):
		self.length = length
		self.width = width
		self.events = []
		if initial_sprite == None:
			self.init = sprite()
		else:
			self.init = initial_sprite

	def c(self):
		output = asciivideo([frame(self.init.c(),0)])
		actuaview = self.init.copy()
		def time(event):return event[2]
		self.events.sort(key=time)
		i=0
		while i < len(self.events):
			time = self.events[i][2]
			while i < len(self.events) and self.events[i][2] == time:
				event = self.events[i]
				event[0](*[actuaview]+event[1])
				i+=1
			output.addFrame(frame(actuaview.c(),time))
		return output 

	def move(self,name,t_i,t_f,r_i,r_f,framerate):
		delta_x = r_f[0]-r_i[0]
		delta_y = r_f[1]-r_i[1]
		delta_t = t_f   -t_i

		def x(t):return floor(r_i[0]+delta_x/delta_t*(t-t_i))
		def y(t):return floor(r_i[1]+delta_y/delta_t*(t-t_i))
		t = framerate*floor(t_i/framerate+1)
		while t < t_f:
			self.events.append([put,[name,[x(t),y(t)]],t])
			t+=framerate

def add(background,thissprite,name,location=None):
	background.add(thissprite,name,location)

def put(background,name,location):
	background.put(name,location)

		

