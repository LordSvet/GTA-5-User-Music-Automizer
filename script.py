import pytube
import os
from moviepy.editor import *


#Function converts the mp4 file to mp3 so that GTA 5 can find it and then deletes the original mp4 file as it's not needed anymore
def mp4Tomp3(original,converted):
    file = AudioFileClip(outputPath + '\\' + original)
    file.write_audiofile(outputPath + '\\' + converted)
    os.remove(outputPath + '\\' + original)
    file.close()
    

#Set output path to your GTA 5 User Music folder. Do not delete the r in front of the string! Then it will throw an exception
outputPath = r'USER_MUSIC_PATH'
#Set the links path to your text file where the youtube links for the songs are
linksPath = r'FILE_WITH_LINKS_PATH'

links = []
with open(linksPath) as linksFile:
    for link in linksFile:
        links.append(link)
        

for link in links:
    try:
        ytLink = pytube.YouTube(link)
        ytLink.streams.get_audio_only().download(outputPath)
        print(ytLink.title + " added!") 
    except Exception as e:
        print(str(e))
        
        
# Convert the mp4 file to mp3 so that the game can actually scan it
for song in os.listdir(outputPath):
    if(not song.endswith('.mp3')):
       mp4Tomp3(song, song + '.mp3')
    print(song + ' got converted to MP3!')
