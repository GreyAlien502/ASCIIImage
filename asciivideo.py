import time

class frame:
	def __init__(self,content,time):
		self.content = content
		self.time = time

class asciivideo:
	def __init__(self,frames=[]):
		self.frames = frames # don't mess with this, sue addFrame

	def minx(self):
		return min([frame.minx() for frame in self.frames])

	def maxx(self):
		return max([frame.maxx() for frame in self.frames])

	def miny(self):
		return min([frame.miny() for frame in self.frames])

	def maxy(self):
		return max([frame.maxy() for frame in self.frames])

	def addFrame(self,frame):
		self.frames.append(frame)
		if frame.time < self.frames[-2].time:
			def time(frame):
				return frame.time
			self.frames.sort(key=time)

	def compile(self,minx=None,miny=None,maxx=None,maxy=None):
		if minx==None: minx=self.minx()
		if maxx==None: maxx=self.maxx()
		if miny==None: miny=self.miny()
		if maxy==None: maxy=self.maxy()

		data = "{:03d}y{:06d}".format(self.length,self.frames)
		for i in range(len(self.frames)-1):
			actuaframe = self.frames[i]
			nextframe  = self.frames[i+1]

			delay = nextframe.time-frame.time
			data += frame.content + delay+"\n"
		return data
	
	def export(self,filepath,length,width):
		f = open(filepath,'r')
		f.write(self.compile())
		f.close()
	
	def play(self):
		for i in range(len(self.frames)-1):
			actuaframe = self.frames[i]
			nextframe  = self.frames[i+1]

			delay = nextframe.time-actuaframe.time
			print(actuaframe.content)
			time.sleep(delay)

'''def decompile(data):
	length= int(data[:3])
	color = data[3]
	frames = int(data[4:10])
	video = data[10:]
	videolecian = video.splitlines()
	output = asciivideo()
	for i in range(0,frames):
		output.addFrame(asciiimage(data,[0,0])

		print('\n'.join(videolecian[i*(length+1):i*(length+1)+length]))
		sleep(float(videolecian[i*(length+1)+length]))
		i+=1
		'''


