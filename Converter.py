import os
import subprocess as s
from moviepy.editor import VideoFileClip

print('''Video To MP3 Converter for Microsoft(R) Windows™
(C)Aniket Maity
All Rights Reserved

This converter will convert the given Video files to MP3 files
''')
input("Press Enter to Continue")

num=0
dirc=os.getcwd()+"\\mp4converter"      #converter folder

#check for existence and modify
while True:
    try:
        os.mkdir(dirc)
        break
    except FileExistsError:
        dirc+=str(num)
        num+=1

#open and wait for user
s.Popen('Explorer "{}"'.format(dirc))
input("\n\nPut the video files in the folder and press enter to continue")

list=os.listdir(dirc)
for i in list:
    try:
        video = VideoFileClip("{}\\{}".format(dirc,i))
        name=i+'.mp3'
        video.audio.write_audiofile("{}\\{}".format(dirc,name))
        video.close()
    except:
        pass

print("\n\nAll video files converted. You may close this application now.")
while True:
    pass