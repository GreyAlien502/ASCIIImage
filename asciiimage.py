import re
import ASCIIImage.manipulate as man

class asciiimage:
	def __init__(self, content,origin = [0,0]):
		self.origin = origin
		self.content = man.complete(content)

	def __str__(self):
		return self.content

	def c(self):
		return self

	def complete(self):
		return asciiimage(man.complete(str(self),self.origin))
			 

	def getWidth(self):
		return str(self).index("\n")

	def getLength(self):
		return str(self).count("\n")

	def expandBounds(self,minx,miny,maxx,maxy):
		image = str(self)
		minxi = -self.origin[0]
		minyi = -self.origin[1]
		maxxi = minxi+self.getWidth()
		maxyi = minyi+self.getLength()
		
		dminx = minx-minxi
		dminy = miny-minyi
		dmaxx = maxx-maxxi
		dmaxy = maxy-maxyi

		if dminx < 0: prex = -dminx
		else: prex = 0
		if dminy < 0: prey = -dminy
		else: prey = 0
		if dmaxx > 0: postx = dmaxx
		else: postx = 0
		if dmaxy > 0: posty = dmaxy
		else: posty = 0
		
		imagelecian = image.splitlines()
		nuvoimagelecian = [(prex+self.getWidth()+postx)*" "]*prey
		nuvoimagelecian.extend([prex*" "+
			imagelecian_item+
			postx*" " 
			for imagelecian_item in imagelecian])
		nuvoimagelecian.extend([(prex+self.getWidth()+postx)*" "]*posty)
		return asciiimage('\n'.join(nuvoimagelecian),[self.origin[0]+prex,self.origin[1]+prey])

	def mirror(self):
		image = str(self)
		mirrorimage = man.mirror(image)
		return asciiimage(image,
			[self.getWidth()-self.origin[0],
			self.getLength()-self.origin[1]])

	def overlay(self,overlaid,x,y):
		nuvoimage = self.expandBounds(
						x-overlaid.origin[0],
						y-overlaid.origin[1],
						x-overlaid.origin[0]+overlaid.getWidth(),
						y-overlaid.origin[1]+overlaid.getLength())
		offsetx = x + nuvoimage.origin[0] - overlaid.origin[0]
		offsety = y + nuvoimage.origin[1] - overlaid.origin[1]

		return asciiimage(man.overlay(str(nuvoimage),str(overlaid),offsetx,offsety),nuvoimage.origin)

	def cropx(self,minx,maxx):
		image = str(self)
		x = self.origin[0]
		w = self.getWidth()
		imagelecian=image.splitlines()
		nuvoimage=""
		if minx < x: prex = x-minx
		else: prex = 0
		if maxx > w+x: postx = w+x-maxx
		else: postx = w+x 

		for imagelecian_item in imagelecian:
			nuvoimage+=imagelecian_item[prex:postx]+'\n'
		return nsciiimage(nuvoimage,[self.origin[0]-prex,self.origin[1]])

	def cropy(self,miny,maxy):
		y = self.origin[1]
		l = self.getLength()
		imagelecian=str(self).splitlines()
		nuvoimage = ""
		if imagelecian == []:
			return "\n"
		else:
			if miny < y: prey = y-miny
			else: prey = 0
			if maxy < l+y: posty = l+y+maxy
			else: posty = l+y
			return "\n"*prey+"\n".join(imagelecian[:posty])

	def crop(self,x,y):
		image = cropy(image,y)
		return cropx(image,x)
