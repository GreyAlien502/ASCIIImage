from asciiimage.asciiimage import asciiimage
from asciiimage.manipulate import *
from asciiimage.asciivideo import asciivideo, frame
from asciiimage.sprite     import sprite
from math import floor

class screen:
	def __init__(self,initial_sprite=None,length=None,width=None):
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
		def time(event):return event[1]
		self.events.sort(key=time)
		i=0
		while i < len(self.events):
			time = self.events[i][1]
			while i < len(self.events) and self.events[i][1] == time:
				event = self.events[i]
				event[0](actuaview)
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
			self.put(t,name,[x(t),y(t)])
			t+=framerate
		t = t_f
		self.put(t,name,[x(t),y(t)])

	def add(self,time,thissprite,name,location=None,index=None):
		def f(bg):
			bg.add(thissprite.copy(),name,location,index)
		self.events.append([f,time])
	
	def remove(self,time,name):
		def f(bg):
			bg.remove(name)
		self.events.append([f,time])
		
	def put(self,time,name,location):
		def f(bg):
			bg[name][2] = location
		self.events.append([f,time])
	
	def cycle(self,name,t_i,t_f,component,statelecian,period):
		states = len(statelecian)
		i=0
		while t_i+period*i < t_f:
			if name == None:
				self.events.append([lambda x,state=statelecian[i%states]:x.setState(component,state),t_i+i*period])
			else:
				self.events.append([lambda x,state=statelecian[i%states],name=name:x[name][0].setState(component,state),t_i+i*period])
			i+=1
