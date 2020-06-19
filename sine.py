#!/usr/bin/env python
from __future__ import division
import math

from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError:  # Python 3
    izip = zip
    xrange = range


def sine_tone(frequency, duration, volume=1.0, sample_rate=44100):
    n_samples = int(sample_rate * duration) #buffer size
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),  # 8bit
                    channels=2,  # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    for buf in izip(*[samples] * sample_rate):  # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()


sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=220.00,  # Hz, waves per second A4
    duration=3.0,  # seconds to play
    volume=.2,  # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=44100  # number of samples per second
)
