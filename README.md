# rtl2832u-theremin
A project to play MIDI tones via my rtlsdl antenna. Uses pyrtlsdr library for prototyping - I want to strip it and write my own bare driver in C since I only need a VERY limited feature set.

## Requirements

* Python 3
* An RTL2832U SDR
* The device to recieve RF proximity I'm going to build
```
$ pip install pyrtlsdr pygame
```

## Current status
Waiting to design/build the RF proximity sensor device.
