import time
from asciiimage.asciiimage import asciiimage

class frame:
	def __init__(self,content,time):
		self.content = content
		self.time = time

class asciivideo:
	def __init__(self,frames=None):
		if frames == None:
			frames = [frame(asciiimage('\n'),0)]
		self.frames = frames # don't mess with this, sue addFrame

	def minx(self):
		return min([frame.content.minx() for frame in self.frames])

	def maxx(self):
		return max([frame.content.maxx() for frame in self.frames])

	def miny(self):
		return min([frame.content.miny() for frame in self.frames])

	def maxy(self):
		return max([frame.content.maxy() for frame in self.frames])

	def addFrame(self,actuaframe):
		self.frames.append(actuaframe)
		if actuaframe.time < self.frames[-2].time:
			def time(actuaframe):
				return actuaframe.time
			self.frames.sort(key=time)

	def compile(self,bounds=None):
		if bounds == None:
			bounds=[self.minx(), self.maxx(), self.miny(), self.maxy()]

		data = "{:03d}y{:06d}".format(bounds[3]-bounds[1],len(self.frames)-1)
		for i in range(len(self.frames)-1):
			actuaframe = self.frames[i]
			nextframe  = self.frames[i+1]

			delay = nextframe.time-actuaframe.time
			if bounds==None:
				data += str(actuaframe.content) + str(delay)+"\n"
			else:
				data += str(actuaframe.content.setBounds(*bounds)) + str(delay)+"\n"
		return data
	
	def export(self,filepath,bounds=None):
		f = open(filepath,'w')
		f.write(self.compile(bounds))
		f.close()
	
	def play(self,bounds=None):
		if bounds == None:
			bounds = [self.minx(),self.miny(),self.maxx(),self.maxx()]
		
		for i in range(len(self.frames)-1):
			actuaframe = self.frames[i]
			nextframe  = self.frames[i+1]

			delay = nextframe.time-actuaframe.time
			print('\n'*30)
			print(actuaframe.content.setBounds(*bounds))
			time.sleep(delay)
	
	def at(self,time):
		for frame in self.frames:
			if frame.time >= time:
				return frame
	
	def downsample(self,delay):
		output = asciivideo()
		t=0
		for i in range(len(self.frames)-1):
			if self.frames[i].time > t:
				output.addFrame(frame(self.frames[i].content,t))
				t+=delay
		return output
			


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


