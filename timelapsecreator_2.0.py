#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

startfile=str(raw_input('Startdatei: '))

filename=str(raw_input('Dateiname (Default  \'IMG_\' ) : '))

name=str(raw_input('Videoname (Default  \'timelapse\' ) : '))

fps=str(raw_input('FPS (Default  \'24\' ) : '))

vidtype=str(raw_input('Videodateiformat (Default  \'.mp4\' ) : '))





if filename =='':
    filename='IMG_'

if name =='':
    name='timelapse'

if fps =='':
    fps='24'

if vidtype =='':
    vidtype='.mp4'

temp=startfile.split(filename)

path=temp[0]


temp=temp[1].split('.')

filetype='.'+temp[1]
startnumber=temp[0]

print(startnumber,filename)

os.chdir(path)

ffname='"'+name+'ffmpeg'+vidtype+'"'

os.system('ffmpeg -r '+fps+' -start_number '+str(startnumber)+' -i '+filename+'%d'+filetype+' -pix_fmt yuv420p '+ffname)

os.system('HandBrakeCLI -i '+ffname+' -o '+name+vidtype)
#os.remove(ffname)



    
