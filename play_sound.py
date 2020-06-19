import pyaudio
import wave
import sys

CHUNK = 1024

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)

while True:
    x = input('Masukkan Nomor: ')
    x = int(x)

    if x == 0:
        wf = wave.open('senang.wav', 'rb')
    elif x == 1:
        wf = wave.open('marah.wav', 'rb')
    elif x == 2:
        wf = wave.open('sedih.wav', 'rb')
    elif x == 3:
        wf = wave.open('netral.wav', 'rb')
    elif x == 4:
        wf = wave.open('terkejut.wav', 'rb')
    elif x == 5:
        wf = wave.open('jijik.wav', 'rb')
    elif x == 6:
        wf = wave.open('takut.wav', 'rb')
    else:
        continue

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()

# close PyAudio (5)
p.terminate()
