import ASCIIImage.manipulate as manipulate
from ASCIIImage.asciiimage import asciiimage

class sprite(asciiimage):
	def __init__(self,n={},state=[],origin = [0,0]):
		self.n = n
		self.state = state
		self.origin = origin
	def __str__(self):
		output = asciiimage('\n')
		for i in range(len(self.state)):
			output = output.overlay(
				self.n[self.state[i][0]],
				self.state[i][1][0],
				self.state[i][1][1])

		return str(output)
	def include(self, path,filename,origin,spacechar = '',alphachar = ''):
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
			name = plecian[0]
			x = int(plecian[1])
			y = int(plecian[2])
			kind = plecian[3]
			if kind == 'asciiimage':
				self.include(path,name,[x,y],plecian[4],plecian[5])
				if len(plecian) == 8:
					X = int(plecian[6])
					Y = int(plecian[7])
					self.state.append([name,[X,Y]])
			if kind == 'sprite':
				actuasprite = sprite({},[])
				actuasprite.be(path+'/'+name)
				actuasprite.origin = [x,y]
				self.n.update({name:actuasprite})
				if len(plecian) == 6:
					X = int(plecian[4])
					Y = int(plecian[5])
					self.state.append([name,[X,Y]])

