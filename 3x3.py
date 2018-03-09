#!python2.7

# python c:\drive\code\3x3.py
import sys,os
import cv2
import moviepy
from moviepy.editor import *
import subprocess, os


args = sys.argv

#if your PC is interrupted while generating clips, run "3x3.py [clip number]" to resume the job.

try:
	print(args)
	x = args[2]
except:
	try:
		x = args[1]
	except:
		x = 1

#place "1.mp4" in your preferred directory
file = "d:/day9/"
file += str(x)
file += ".mp4"


clip1 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((0,0)).resize((1280,720))

clip2 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((1280,0)).resize((1280,720))
	
clip3 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((2560,0)).resize((1280,720))

clip4 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((0,720)).resize((1280,720))

clip5 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((1280,720)).resize((1280,720))

clip6 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((2560,720)).resize((1280,720))

clip7 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((0,1440)).resize((1280,720))

clip8 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((1280,1440)).resize((1280,720))

clip9 = VideoFileClip(file, audio_buffersize=1000000000 ).set_position((2560,1440)).resize((1280,720))

#This is the distance on which clips will be overlayed
y = 0.11

video = CompositeVideoClip([clip1, clip2.set_start(y), clip3.set_start(y*2), clip4.set_start(y*3), clip5.set_start(y*4), clip6.set_start(y*5), clip7.set_start(y*6), clip8.set_start(y*7), clip9.set_start(y*8)],  size = (3840,2160))

x = int(x)
x += 1


sd=0
xdd = 20
z=20
c = 1
#The Z limit is the total duration of ALL generated clips combined, in seconds. In other words: With a value of 36000, the script will stop once 10 hours of clips has been generated.
while z <36000:
	
	sd = xdd + (y*8)
	z+= sd
	xdd = sd
	c+=1
c+=1
f = 2


video = video.volumex(.99)
filename = "d:/day9/"
filename+= str(x)
filename+= ".mp4"
xd = "saving video number "

xd += str(x)
print(xd)
print(" out of ")
print(c)


video.write_videofile(filename,fps=f, codec='mpeg4')


#change "c:\\3x3.py" to your directory
if x  < c:
	cmd = "start c:\python27\python c:\\3x3.py "
	cmd += str(x)
	os.system(cmd)
	