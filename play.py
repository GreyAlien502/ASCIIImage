#!/usr/bin/env python3

from time import sleep
from sys import argv

filename = argv[1]
jad = open(filename,'r')
data = jad.read()
length= int(data[:3])
color = data[3]
frames = int(data[4:10])
video = data[10:]
videolecian = video.splitlines()
for i in range(0,frames):
	print('\n'*29)
	print('\n'.join(videolecian[i*(length+1):i*(length+1)+length]))
	sleep(float(videolecian[i*(length+1)+length]))
	i+=1
