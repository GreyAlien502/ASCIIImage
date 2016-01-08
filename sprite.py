import ASCIIImage.manipulate as manipulate
from ASCIIImage.asciiimage import asciiimage

class sprite:
	def __init__(self,path=None,components=None):
		if components == None: self.components = []
		else: self.components = components

		if path != None:
			self.be(path)
		self.parent = None

	def __str__(self):
		return str(self.c())
	
	def __len__(self):
		return len(self.components)
	
	def __getitem__(self,key):
		if type(key) == int:
			return self.components[key]
		elif type(key) == str:
			return self.components[self.getIndex(key)]
		elif type(key) == slice:
			indexes = key.indices(len(self.components))
			i=indexes[0]
			output = []
			while i > indexes[1]:
				output.append(self[i])
				i+=indexes[2]
			return output

	def __setitem__(self,key,value):
		if type(key) == int:
			self.components[key] = value
		elif type(key) == str:
			self.components[self.getIndex(key)] = value
		elif type(key) == slice:
			indexes = key.indices(len(self.components))
			i=indexes[0]
			while i > indexes[1]:
				self[i]=value[i]
				i+=indexes[2]
			return output

	def __delitem__(self,key):
		if type(key) == int:
			del self.components[key]
		elif type(key) == str:
			del self.components[self.getIndex(key)]
		elif type(key) == slice:
			indexes = key.indices(len(self.components))
			i=indexes[0]
			while i > indexes[1]:
				del self[i]
				i+=indexes[2]

	def c(self):
		output = asciiimage('\n')
		for component in self:
			if component[2]!= None:
				output = output.overlay(
					component[0].c(),
					component[2][0],
					component[2][1])

		return output
	
	def copy(self):
		copied = sprite()
		for component in self:
			if type(component[0]) == asciiimage:
				copied.add(*component)
			else:
				copied.add(component[0].copy(),component[1],component[2])
		return copied

	def  be(self, path):
		f = open(path+"/list",'r')
		filelecian = f.read().splitlines()
		f.close()
		for filelecian_item in filelecian:
			plecian = filelecian_item.split('\t')
			kind = plecian[0]
			name = plecian[1]
			location = None
			if kind == 'asciiimage':
				x = int(plecian[2])
				y = int(plecian[3])
				spacechar = plecian[4]
				alphachar = plecian[5]

				addfile = open(path+'/'+name,'r')
				image = addfile.read()
				addfile.close()
		
				if spacechar != '':
					image = image.translate(''.maketrans(spacechar,'\u00A0'))
				if alphachar != '':
					image = image.translate(''.maketrans(alphachar,' '))
				content = asciiimage(image,[x,y])

				if len(plecian) == 8:
					X = int(plecian[6])
					Y = int(plecian[7])
					location = [X,Y]
			elif kind == 'sprite':
				content = sprite(path+'/'+name)
				if len(plecian) == 4:
					X = int(plecian[2])
					Y = int(plecian[3])
					location=[X,Y]
			self.add(content,name,location)

	def getIndex(self,name):
		return next(i for i in range(len(self)) if self[i][1] == name)
	
	def active(self):
		return next(component for component in self if component[2] != None)

	def add(self,actuasprite,name,location=None,index=None):
		if index ==None:
			self.components.append([actuasprite,name,location])
		else:
			self.components.insert(index,[actuasprite,name,location])
		actuasprite.parent = self

	def put(self,name,location):
		self[name][2] = location

	def setIndex(self,name,index):
		components = self.components
		components.insert(index, components.pop(self.getIndex(name)))
	
	def remove(self,name):
		self[name][0].parent = None
		del self[name]
	
	def replace(self,old,new,position=None):
		if position == None:
			position = self[old][2]
		self[old][2] = None
		self[new][2] = position
	
	def setState(self,component,state,position=None):
		target = self[component][0]
		target.replace(target.active()[1],state,position)
