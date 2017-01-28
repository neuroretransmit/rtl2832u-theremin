#!/usr/bin/env python3

from rtlsdr import RtlSdr

sdr = RtlSdr()

sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

midi_player = Midi(0)

while True:
	for sample in sdr.read_samples(512):
                midi_player.play(0, sample, 1)


