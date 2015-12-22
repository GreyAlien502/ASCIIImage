import time

class frame:
	def __init__(self,content,time,formatt='n'):
		self.content = content
		self.time = time

class asciivideo:
	def __init__(self,frames=[],formatt='n'):
		for frame in frames:
			if frame.formatt!=formatt:
				print('error')
		self.frames = frames
	
	def sort(self):
		def time(frame):
			return frame.time
		self.frames.sort(key=time)
	
	def compile(self):
		self.sort()

		data = "{:03d}y{:06d}".format(self.length,self.frames)
		for i in range(len(self.frames)-1):
			actuaframe = self.frames[i]
			nextframe  = self.frames[i+1]

			delay = nextframe.time-frame.time
			data += frame.content + delay+"\n"
		return data

	def export(self,filepath):
		f = open(filepath,'r')
		f.write(self.compile())
		f.close()
	
	def play(self):
		self.sort()

		for i in range(len(self.frames)-1):
			actuaframe = self.frames[i]
			nextframe  = self.frames[i+1]

			delay = nextframe.time-actuaframe.time
			print(actuaframe.content)
			time.sleep(delay)
