import ASCIIImage.manipulate as manipulate
from ASCIIImage.asciiimage import asciiimage

class sprite:
	def __init__(self,path=None,components=None):
		if components == None: self.components = []
		else: self.components = components

		if path != None:
			self.be(path)

	def __str__(self):
		return str(self.c())

	def c(self):
		output = asciiimage('\n')
		for component in self.components:
			if component[1]!= None:
				output = output.overlay(
					component[0].c(),
					component[1][0],
					component[1][1])

		return output
	
	def copy(self):
		components = []
		for component in self.components:
			if type(component) == asciiimage:
				contents.append(component)
			else:
				components.append(component.copy())
		return sprite(None,components)

	def  be(self, path):
		f = open(path+"/list",'r')
		filelecian = f.read().splitlines()
		f.close()
		for filelecian_item in filelecian:
			plecian = filelecian_item.split('\t')
			kind = plecian[0]
			name = plecian[1]
			if kind == 'asciiimage':
				x = int(plecian[2])
				y = int(plecian[3])
				spacechar = plecian[4]
				alphachar = plecian[5]

				addfile = open(path+'/'+plecian[1],'r')
				image = addfile.read()
				addfile.close()

				location = None
				if len(plecian) == 8:
					X = int(plecian[6])
					Y = int(plecian[7])
					location = [X,Y]
		
				if spacechar != '':
					image = image.translate(''.maketrans(spacechar,'\u00A0'))
				if alphachar != '':
					image = image.translate(''.maketrans(alphachar,' '))
				content = asciiimage(image,[x,y])
			elif kind == 'sprite':
				content = sprite(path+'/'+name)
				self.components.append([{name:actuasprite},None])
				location = None
				if len(plecian) == 6:
					X = int(plecian[4])
					Y = int(plecian[5])
					location=[X,Y]
			self.add(content,location)

	def add(self,sprite,location=None):
		self.components.append([sprite,location])
			

	def put(self,actuasprite,location):
		spritenum = next(i for i in len(self.components) if self.components[i][0] == actuasprite)
		self.components[spritenum][1] = location
