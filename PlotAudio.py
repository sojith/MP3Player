import matplotlib.pyplot as plt
import wave
import io

# Audio signal parameters
# - number of channels (1 - mono, 2- stereo)
# - sample width - number of Bytes in each sample
# - framerate/sample_rate - number of samples per second E.g. 44,100 Hz
# - number of frames - total number of frames
# - values of a frame -  values in each fram (in binary format; can be converted to integer values)

obj = wave.open("StarWars3.wav","rb")
print("Number of channels", obj.getnchannels())
print("Sample Width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("Number of Frames", obj.getnframes())
print("All Params", obj.getparams())

t_audio = obj.getnframes()/obj.getframerate()

print("Time of Audio", t_audio)

x = 0
y_data = []
x_data = []
frames = obj.readframes(-1)
print(len(frames))
#print(frames)
file = io.BytesIO(frames)
for i in range(obj.getnframes() ):
	y_data.append( int.from_bytes(file.read(2), "little", signed="True") )	
#	print( int.from_bytes(file.read(2), "little", signed="True")  )
	x_data.append(  i/obj.getframerate() )
plt.plot(x_data, y_data)
plt.show()

obj.close()
