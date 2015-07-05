import ASCIIImage.manipulate as manipulate
from ASCIIImage.asciiimage import asciiimage

class sprite:
	def __init__(self,n=None,state=None):
		if n == None: self.n = {}
		else: self.n = n
		
		if state == None: self.state = []
		else: self.state = state
	def __str__(self):
		return str(self.c())
	def c(self):
		output = asciiimage('\n')
		for i in range(len(self.state)):
			output = output.overlay(
				self.n[self.state[i][0]].c(),
				self.state[i][1][0],
				self.state[i][1][1])

		return output
	def include(self,path,filename,origin,spacechar = '',alphachar = ''):
		addfile = open(path+'/'+filename,'r')
		image = addfile.read()
		
		if spacechar != '':
			image = image.translate(''.maketrans(spacechar,'\u00A0'))
		if alphachar != '':
			image = image.translate(''.maketrans(alphachar,' '))
		self.n.update({filename:asciiimage(image,origin)})
	def  be(self, path):
		filelecian = open(path+"/list",'r').read().splitlines()
		for filelecian_item in filelecian:
			plecian = filelecian_item.split('\t')
			kind = plecian[0]
			name = plecian[1]
			if kind == 'asciiimage':
				x = plecian[2]
				y = plecian[3]
				spacechar = plecian[4]
				alphachar = plecian[5]
				self.include(path,name,[x,y],spacechar,alphachar)
				if len(plecian) == 8:
					X = int(plecian[6])
					Y = int(plecian[7])
					self.state.append([name,[X,Y]])
			if kind == 'sprite':
				actuasprite = sprite()
				actuasprite.be(path+'/'+name)
				self.n.update({name:actuasprite})
				if len(plecian) == 6:
					X = int(plecian[4])
					Y = int(plecian[5])
					self.state.append([name,[X,Y]])

