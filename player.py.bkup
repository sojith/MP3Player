import tkinter
from tkinter import filedialog
import ffmpeg
import wave
import pyaudio

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
	if len(playlist_files) >= 1:
		if current_pos < (len(playlist_files)-1) and movement == 1:
			current_pos = current_pos + 1
			canvas.itemconfig(playlist_file_pos[current_pos], fill="green3")
			canvas.itemconfig(playlist_file_pos[current_pos-movement], fill="green")
		if current_pos > 0 and movement == -1:
			current_pos = current_pos -1
			canvas.itemconfig(playlist_file_pos[current_pos], fill="green3")
			canvas.itemconfig(playlist_file_pos[current_pos-movement], fill="green")


def playFile(filename):
	print ("Playing file " + filename)
	inter = ffmpeg.input(filename)
	stream = ffmpeg.output(inter, "test2.wav")
	ffmpeg.run(stream)

	wf = wave.open("test2.wav", "rb")

	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

	WIDTH=1024

	data = wf.readframes(WIDTH)

	while len(data):
	    stream.write(data)
	    data = wf.readframes(WIDTH)

	stream.stop_stream()
	stream.close()

	p.terminate()
	print("MP3 over")


playlist_pos_y = 50	#coordinates of each file inthe playlist
playlist_files = []	#names of files in the playlist
playlist_file_pos = []	#position assigned to each file in the playlist
current_pos = 0		#position of the currently selectd file inthe playlist
wind = tkinter.Tk()
wind.geometry("420x350")
wind.resizable(False,False)

canvas=tkinter.Canvas(wind, width=700, height=420, bg="black")
canvas.pack()

canvas.create_text(10,20, text="Playlist", anchor="w", fill="green3", font=('Dustismo','12', 'bold'))

#Select Button
selBtn = tkinter.Button(canvas, text="Select", background="dim gray", activebackground="slate gray", highlightthickness=0, command=selectButtonFunc)
selBtn.place(x=10, y=310)

#Forward
forwardBtn = tkinter.Button(canvas, text="Forward", background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: movePositionFunc(1))
forwardBtn.place(x=90, y=310)

#Backward
backwardBtn = tkinter.Button(canvas, text="Backward", background="dim gray", activebackground="slate gray", highlightthickness=0, command=lambda: movePositionFunc(-1))
backwardBtn.place(x=190, y=310)

#btn.pack()

wind.update()
wind.mainloop()

print(playlist_file_pos)
