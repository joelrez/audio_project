# audio_projects

## Introduction
In this project, I am simulating recordings to better understand sound and signal processing. I have two interests in this subject:
* I want to understand music more. I was inspired by the creation of new musical instruments such as the [harpeji](https://www.youtube.com/watch?v=Wr87Z7rZiWE). I wonder why exactly we need to limit ourselves to simple traditional instruments. ![image](https://github.com/joelrez/audio_project/assets/32008471/5aa25593-cf49-4712-8e9a-b0f5fea54bc2)
* I want to understand how the sound coming from an object moving around in a space affects the audio recording. For this, I am attempting to apply the [inverse square law](https://en.wikipedia.org/wiki/Inverse-square_law) to an object moving in a 2D space where it is assumed we know the locations of the object and microphone, but we (I) don't know how the signal attenuates given the distance.

## Musical Notes
To start, we must understand what musical notes even are, which in theory are essentially frequencies. The following formula is used to generate the waveform of the note.

y(t) = Asin(2&pi;ft) where y(t) is the signal, t is time, and f is the frequency.

For example take for instance a frequency of 2, we would have the following

y(t) = 127sin(2&pi;(2t))

This means that there are 2 cycles per second, i.e. the following figure will have exactly 2 cycles over the duration of 1 second.
![image](https://github.com/joelrez/audio_project/assets/32008471/2ab2bfb9-1f9e-4a17-a699-88ede503999a)

And for a note A4 or the A note in the 4th octave, we have a frequency of 440 (to find other note frequencies check [here](https://muted.io/note-frequencies/).) Below we can see it's not super easy to analyze this 1 second note since we're looking at the sound recording at a much higher frequency.
![image](https://github.com/joelrez/audio_project/assets/32008471/bd2805a4-e671-48c5-9e9a-5dd4a7074696)

One note (badum-tst), if you checked out the frequencies chart for each note, each octave is twice the previous octave. For example, if I want to change a note A4 to an AN<sup>th</sup> octave, then I would use the following to find the new frequency.

f<sub>AN</sub> = f<sub>A4</sub>(2<sup>N-4</sup>)

Let N = 2, i.e., A2. Then f<sub>A2</sub> = f<sub>A4</sub>(2<sup>2-4</sup>) = f<sub>A4(</sub>2<sup>-2</sup>) = f<sub>A4</sub>/4 As we'd expect.

This lead me to think about the potential of creating a sort of algebra with musical notes.

One such operation I used to generate /audio_files/jinglebells.wav is assembling these one second notes (which are like the wave forms presented above) into a block matrix, which would be the entire recording.

```py
  num_channels    = 1                             # mono audio
  sample_width    = 2                            # 8 bits(1 byte)/sample
  sample_rate     = 44.1e3                        # 44.1k samples/second
  frequency       = 233.08                          # 440 Hz
  duration        = 20                            # play for this many seconds

  n = round(sample_rate/frequency)
  periods = round(frequency*duration)
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

  E = getNote('E4')
  silence = 0*t
  G = getNote('G4')
  C = getNote('C4')
  D = getNote('D4')
  F = getNote('F4')
  A = getNote('A4')
  B = getNote('B4')
  data = (127*np.block([E, E, E, silence,
                        E, E, E, silence,
                        E, G, C, D, E, F, F, F, F, silence,
                        F, E, E, E, E, G, G, F, D, C])).astype(np.int8)
```
