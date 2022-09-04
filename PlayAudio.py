import ffmpeg
import wave
import pyaudio
import io

inter = ffmpeg.input('the-last-piano.mp3')
stream = ffmpeg.output(inter, "test2.wav")
ffmpeg.run(stream)

wf = wave.open("test2.wav", "rb")
print("Number of channels", wf.getnchannels())
print("Sample Width", wf.getsampwidth())
print("Frame Rate", wf.getframerate())
print("Number of Frames", wf.getnframes())
print("All Params", wf.getparams())

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


