import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy import signal
import librosa

num_channels    = 1                             # mono audio
sample_width    = 2                            # 8 bits(1 byte)/sample
sample_rate     = 44.1e3                        # 44.1k samples/second

# Create a single period of sine wave.
t = np.linspace(0.0, 1, int(sample_rate))

freqs = { 'C' : 261.63,
          'C#' : 277.18,
          'D' : 293.66,
          'D#' : 311.13,
          'E' : 329.63,
          'F' : 349.23,
          'F#' : 369.99,
          'G' : 392,
          'G#' : 415.3,
          'A' : 440,
          'A#' : 466.16,
          'B' : 493.88
        }

def getNote(note):
    note_ = note[0:-1]
    octave = int(note[-1])
    return np.sin(2*t*np.pi*freqs[note_]*2**(octave - 4))

def compile(notes):
    return (127*np.block(notes)).astype(np.int8)

def save(filename, data):
    # open WAV file and write data
    with wave.open('audio_files/'+filename+'.wav', 'w') as wavfile:
        
        wavfile.setnchannels(num_channels)
        wavfile.setsampwidth(sample_width)
        wavfile.setframerate(sample_rate)
    
        wavfile.writeframes(data)