import ASCIIImage.manipulate as manipulate
import ASCIIImage.asciiimage as asciiimage

class sprite(asciiimage):
	def __init__(self,n,state):
		self.n = n
		self.state = state
	def __str__(self):
		output = "\n"
		for i in range(len(self.state)):
			output = manipulate.overlay(
				output,
				str(self.n[self.state[i][0]]),
				self.state[i][1],
				self.state[i][2])
		return output
	def add(filename,spacechar = ''):
		addfile = open(name,'r')
		contents = addfile.read()
		displayname = name[-name[::-1].index('/'):]
		if spacechar != '':
			addcontent = addcontent.translate(''.maketrans(ispacechar,'\u00A0'))
		self.n.update({displayname:addcontents})

