import re

def replace_all(text,dic):
	map = {ord(k): ord(v) for k, v in dic.items()}
	inv_map = {ord(v): ord(k) for k, v in dic.items()}
	map.update(inv_map)
	return text.translate(map)

def complete(image):
	imagelecian = image.splitlines()
	width = max([len(i) for i in image.splitlines()])
	nuvoimage = ""
	for imagelecian_item in imagelecian:
		spacenum = width-len(imagelecian_item)
		nuvoimage += imagelecian_item+" "*spacenum +"\n"
	return nuvoimage
		 

def getWidth(image):
	return image.index("\n")

def getLength(image):
	return image.count("\n")

def setSize(image,x,y):
	width = image.index("\n")
	length = getLength(image)
	if x > width:
		image = image[:width]+" "*(x-width)+image[width:]
		image = complete(image)
	if y > length:
		image = image+(" "*x+"\n")*(y-length)
	return image

def mirror(image):
	image = complete(image)	
	imagelecian = image.splitlines()
	nuvoimage = ""
	for imagelecian_item in imagelecian:
		reverse = imagelecian_item[::-1]
		reverse = replace_all(reverse,
			{"/":"\\",
			"<":">",
			",":"."})
		nuvoimage+=reverse+"\n"
	return nuvoimage

def overlay(image,overlaid,x,y):
	overlecian = overlaid.splitlines()
	wimage = getWidth(image)
	limage = getLength(image)
	wover = getWidth(overlaid)
	lover = getLength(overlaid)
	image = setSize(image,x+wover,y+lover)

	overlecian = overlaid.splitlines()
	imagelecian = image.splitlines()
	if y==0:
		nuvoimage=""
	else:
		nuvoimage = "\n".join(imagelecian[:y])+"\n"
	for i in range(0,lover):
		nuvoimage += imagelecian[y+i][:x]
		for j in range(0,len(overlecian[i])):
			if overlecian[i][j] != " ":
				nuvoimage+=overlecian[i][j]
			else:
				nuvoimage+=imagelecian[y+i][x+j]
		nuvoimage+=imagelecian[y+i][x+j+1:]+"\n"
	nuvoimage += "\n".join(imagelecian[y+lover:])
	return nuvoimage




'''	actuay = y
	
	nuvoimage = image[:actuay*wimage]
	for i in range(0,len(overlecian)):
		actuax = x
		nuvoimage += image[actuay*wimage:actuay+actuax]
		deltaactuax = overlecian[i][actuax:].find(" ")
		while actuax + x < len(overlecian[i]):
			if deltaactuax == -1:
				nuvoimage+=overlecian[i][actuax-x:]
				break
			nuvoimage+=overlecian[i][actuax-x:actuax-x+deltaactuax]+" "
			actuax += nuvoactuax
			deltaactuax = overlecian[i][actuax:].find(" ")
		actuay+=1
'''

def extend(image,x):
	imagelecian = image.splitlines()
	output = ""
	for i in range(0,len(imagelecian)):
		output = output +imagelecian[i]+ " "*x+"\n"
	return output

def append(image1, image2):
	length1 = image1.count("\n")
	length2 = image2.count("\n")
	if (length2 < length1):
		image2 = complete(image2+(length1-length2)*"\n")
		length2 = length1
	else:
		image1 = complete(image1+(length2-length1)*"\n")
		length1 = length2
	image1lecian = image1.splitlines()
	image2lecian = image2.splitlines()
	
	nuvoimage = ""

	for i in range(0,length1):
		nuvoimage += image1lecian[i]+image2lecian[i]+"\n"
	return nuvoimage

def cropx(image,x):
	imagelecian=image.splitlines()
	nuvoimage=""
	for imagelecian_item in imagelecian:
		nuvoimage+=imagelecian_item[:x]+'\n'
	return nuvoimage

def cropy(image,y):
	imagelecian=image.splitlines()
	if imagelecian == []:
		return "\n"
	else:
		return "\n".join(imagelecian[:y])

def crop(image,x,y):
	image = cropy(image,y)
	return cropx(image,x)
