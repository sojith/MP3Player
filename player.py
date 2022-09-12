import tkinter
from tkinter import filedialog
import ffmpeg
import wave
import pyaudio
import os
import threading

def selectButtonFunc():
	global playlist_pos_y
	global playlist_files
	#print("Button1 clicked")	#Debug
	f = tkinter.filedialog
	filename = f.askopenfilename()
	#print(filename)		#Debug
	ext=filename[len(filename)-3:]
	if ext == "mp3":
		#playFile(filename)
		#print(len(playlist_files))
		try:
			if playlist_files.index(filename) >= 0:
				print(filename + " - This file is in the playlist already")

		except:
			if len(playlist_files) < 7:
				playlist_files.append(filename)
				if len(playlist_files) == 1:
					playlist_file_pos.append( canvas.create_text(10,playlist_pos_y, text=filename, anchor="w", fill="green3", font=('Dustismo','10')) )
				else:
					playlist_file_pos.append( canvas.create_text(10,playlist_pos_y, text=filename, anchor="w", fill="green", font=('Dustismo','10')) )
				playlist_pos_y+=20
			else:
				print("Playlist size exceeeded")
	else:
		print("This is not an mp3 file")
#	print(playlist_files)		#Debug

def movePositionFunc(movement):
	global current_pos
	global playlist_files
	global playlist_file_pos
	global playStatus
	if len(playlist_files) >= 1 and playStatus == 0:
		if current_pos < (len(playlist_files)-1) and movement == 1:
			current_pos = current_pos + 1
			canvas.itemconfig(playlist_file_pos[current_pos], fill="green3")
			canvas.itemconfig(playlist_file_pos[current_pos-movement], fill="green")
		if current_pos > 0 and movement == -1:
			current_pos = current_pos -1
			canvas.itemconfig(playlist_file_pos[current_pos], fill="green3")
			canvas.itemconfig(playlist_file_pos[current_pos-movement], fill="green")


def playFile(filename):
	global playStatus
	global pauseStatus
	try:
		os.remove("test2.wav")
	except:
		print("file removed")
	print ("Playing file " + filename)
	inter = ffmpeg.input(filename)
	stream = ffmpeg.output(inter, "test2.wav")
	ffmpeg.run(stream)

	wf = wave.open("test2.wav", "rb")

	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

	WIDTH=1024

	data = wf.readframes(WIDTH)

	playStatus = 1
	pauseStatus = 0

	print("Pause Status ", pauseStatus)
	while len(data) and playStatus == 1:
		if pauseStatus == 0:
		    stream.write(data)
		    data = wf.readframes(WIDTH)
		else:
			pass
	stream.stop_stream()
	stream.close()

	p.terminate()
	playStatus = 0		# i.e. nothing is playing anymore
	pauseStatus = 0		# i.e. nothing is paused anymore
	print("MP3 over")

def playBtnClicked(filename):
	if filename and playStatus == 0:
		t1 = threading.Thread(target=playFile, args=(filename,))
		t1.start()

def stopBtnClicked():
	global playStatus
	playStatus = 0
	pauseBtn.configure(background="dim gray", activebackground="slate gray")

def pauseBtnClicked():
	global pauseStatus
	global playStatus
	if playStatus == 1 and pauseStatus == 0:
		pauseStatus = 1
		pauseBtn.configure(background="dark slate blue", activebackground="slate blue")
	elif playStatus == 1 and pauseStatus == 1:
		pauseStatus = 0
		pauseBtn.configure(background="dim gray", activebackground="slate gray")



playlist_pos_y = 50	#coordinates of each file inthe playlist
playlist_files = []	#names of files in the playlist
playlist_file_pos = []	#position assigned to each file in the playlist
current_pos = 0		#position of the currently selectd file inthe playlist
playStatus = 0 		#Current of Play. 0 is not playing. 1 is playing
pauseStatus = 0		#Current status of Pause. 1 is Paused
wind = tkinter.Tk()
wind.geometry("420x350")
wind.resizable(False,False)

canvas=tkinter.Canvas(wind, width=700, height=420, bg="black")
canvas.pack()

canvas.create_text(10,20, text="Playlist", anchor="w", fill="green3", font=('Dustismo','12', 'bold'))

#Create images
selImg=tkinter.PhotoImage(file='./icons/eject.png')
selImg.configure(width=32, height=32)

nextTrackImg=tkinter.PhotoImage(file='./icons/nextTrack.png')
nextTrackImg.configure(width=32, height=32)

previousTrackImg=tkinter.PhotoImage(file='./icons/previousTrack.png')
previousTrackImg.configure(width=32, height=32)

playImg=tkinter.PhotoImage(file='./icons/play.png')
playImg.configure(width=32, height=32)

stopImg=tkinter.PhotoImage(file='./icons/stop.png')
stopImg.configure(width=32, height=32)

pauseImg=tkinter.PhotoImage(file='./icons/pause.png')
pauseImg.configure(width=32, height=32)



#Select Button
#selBtn = tkinter.Button(canvas, text="Select", background="dim gray", activebackground="slate gray", highlightthickness=0, command=selectButtonFunc)
selBtn = tkinter.Button(canvas, image=selImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=selectButtonFunc)
selBtn.place(x=10, y=305)

#Backward
#backwardBtn = tkinter.Button(canvas, text="Backward", background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: movePositionFunc(-1))
backwardBtn = tkinter.Button(canvas, image=previousTrackImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: movePositionFunc(-1))
backwardBtn.place(x=50, y=305)

#Play
#playBtn = tkinter.Button(canvas, image=playImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: playFile(playlist_files[current_pos]))
playBtn = tkinter.Button(canvas, image=playImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: playBtnClicked(playlist_files[current_pos]))
playBtn.place(x=90, y=305)

#Forward
#nextTrackBtn = tkinter.Button(canvas, text="Forward", background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: movePositionFunc(1))
previousTrackBtn = tkinter.Button(canvas, image=nextTrackImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: movePositionFunc(1))
previousTrackBtn.place(x=130, y=305)

#Stop
stopBtn = tkinter.Button(canvas, image=stopImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=stopBtnClicked)
stopBtn.place(x=170, y=305)

#Pause
pauseBtn = tkinter.Button(canvas, image=pauseImg, background="dim gray", activebackground="slate gray", highlightthickness=0, command=pauseBtnClicked)
pauseBtn.place(x=210, y=305)

#btn.pack()

wind.update()
wind.mainloop()

print(playlist_file_pos)
