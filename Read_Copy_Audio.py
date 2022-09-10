import wave

# Audio signal parameters
# - number of channels (1 - mono, 2- stereo)
# - sample width - number of Bytes in each sample
# - framerate/sample_rate - number of samples per second E.g. 44,100 Hz
# - number of frames - total number of frames
# - values of a frame -  values in each fram (in binary format; can be converted to integer values)

obj = wave.open("PinkPanther60.wav","rb")
print("Number of channels", obj.getnchannels())
print("Sample Width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("Number of Frames", obj.getnframes())
print("All Params", obj.getparams())

t_audio = obj.getnframes()/obj.getframerate()

print("Time of Audio", t_audio)
frames = obj.readframes(-1)
print("Data Type of Frames - " , type(frames), "     Data type of each frame - " ,type(frames[1]))
print("Length of Frames (Equal to total number of bytes)- ", len(frames))

obj.close()

#Creating a new audio .wav file, which will be a copy of the above .wav file
obj_new = wave.open("Copy.wav","wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(22050)
obj_new.setnframes(1323000)
obj_new.writeframes(frames)
obj_new.close()
