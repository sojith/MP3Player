import tkinter
import time
import threading

class Bars:
	def __init__(self, x, y, movement, delay, wind, canvas, colour):
		self.x1=x
		self.y1=y
		self.movement1=movement
		self.delay1=delay
		self.wind1=wind
		self.canvas1=canvas
		self.colour1=colour
		self.colour_top=colour
		self.colour_below="black"
		self.rect = self.canvas1.create_oval(self.x1,self.y1,self.x1+40,self.y1+40, fill=self.colour_top)
#
	def animation(self):
		while True:
			time.sleep(self.delay1)
			if self.canvas1.coords(self.rect)[1] < 10:
				self.movement1=1

			if self.canvas1.coords(self.rect)[3] > 346:
				self.movement1=-1

			self.canvas1.move(self.rect,0,self.movement1)
#			self.y1=self.y1+self.movement1
#			self.rect = self.canvas1.create_rectangle(self.x1,self.y1,self.x1+40,self.y1+40, fill=self.colour_top)

			self.wind1.update()
			self.wind1.mainloop

def activate(e):
	global counter
	if counter < len(bar):
		print("This is Bar",counter)
		t1 = threading.Thread(target=bar[counter].animation)
		t1.start()
		counter=counter+1
	else:
		print("no more bars left")

wind = tkinter.Tk()
wind.geometry("420x350")
wind.resizable(False,False)

canvas=tkinter.Canvas(wind, width=700, height=420)
canvas.configure(bg="Black")
canvas.pack()

bar = [None]*7
bar[0]=Bars(x=10, y=350, movement=-1, delay=0.5, wind=wind, canvas=canvas, colour="green3")
bar[1]=Bars(x=70, y=350, movement=-2, delay=0.1, wind=wind, canvas=canvas, colour="blue3")
bar[2]=Bars(x=130, y=350, movement=-2, delay=0.05, wind=wind, canvas=canvas, colour="yellow3")
bar[3]=Bars(x=190, y=350, movement=-2, delay=0.01, wind=wind, canvas=canvas, colour="red3")
bar[4]=Bars(x=250, y=350, movement=-2, delay=0.005, wind=wind, canvas=canvas, colour="brown3")
bar[5]=Bars(x=310, y=350, movement=-2, delay=0.001, wind=wind, canvas=canvas, colour="green")
bar[6]=Bars(x=370, y=350, movement=-2, delay=0.0005, wind=wind, canvas=canvas, colour="blue")

counter=0


value1=wind.bind('<a>',activate)

wind.mainloop()

