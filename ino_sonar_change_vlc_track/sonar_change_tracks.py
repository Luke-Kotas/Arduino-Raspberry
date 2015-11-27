import serial 
import os
#import time
#import thread
#from threading import Thread
import vlc



s1 = "/home/ermis/Videos/4K Video Downloader/Ray Charles - If You Go Away (LIVE) HD.mp4"
s2 = "/home/ermis/Videos/4K Video Downloader/Cake - i will survive.mp4"
s3 = "/home/ermis/Videos/4K Video Downloader/Beck - Loser.mp4"
s4 = "/home/ermis/Videos/4K Video Downloader/Neil Diamond - If You Go Away. with LYRICS.mp4"
s5 = "/home/ermis/Videos/4K Video Downloader/El Choclo (Tango) - Eduardo Rojas - Piano on Fire.mp4"
s6 = "/home/ermis/Videos/4K Video Downloader/Celos ( Tango).mp4"
s7 = "/home/ermis/Videos/4K Video Downloader/Pink Martini Donde Estas, Yolanda.mp4"
s8 = "/home/ermis/Videos/4K Video Downloader/Pink Martini - Una Notte a Napoli.mp4"
s9 = "/home/ermis/Videos/4K Video Downloader/CESARIA EVORA Historia De Un Amor..wmv.mp4"
s10 = "/home/ermis/Videos/4K Video Downloader/Cuba Feliz - Lagrimas Negras (Lyric added).mp4"
s11 = "/home/ermis/Videos/4K Video Downloader/Elvis Presley-A Little Less Conversation.mp4"

songs = [s1,s4,s5,s6,s7,s8,s9,s10,s11,s2,s3]

ser = serial.Serial('/dev/ttyACM0', 9600)
i = 0

playSong = vlc.MediaPlayer(songs[0])

while(1):
	a = ser.readline()
	b = a.split()
	distance = int(b[1])
	print a
	if(distance > 0 and distance <= 20):
		playSong.stop()
	elif(distance > 20 and distance <= 40 ):
		# forward
		i += 1
		if(i >= 0 and i < len(songs)):
			playSong.stop()
			playSong = vlc.MediaPlayer(songs[i]) 
			playSong.play()
		else:
			i -= 1	
		
		
	elif(distance> 40 and distance< 100 ):
		i -= 1
		if(i >= 0 and i < len(songs)):
			playSong.stop()
			playSong = vlc.MediaPlayer(songs[i])
			playSong.play()
		else:
			i+=1
		
		
