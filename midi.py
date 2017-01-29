#!/usr/bin/env python

import pygame.midi
import time

class Midi:
    def __init__(self, output_num):
        self.output_num = output_num
        pygame.midi.init()
        self.player = pygame.midi.Output(output_num)

    def play(self, instrument, note, duration):
        self.instrument = instrument
        self.player.set_instrument(instrument)
        self.player.note_on(note, 127)
        time.sleep(duration)
        self.player.note_off(note, 127)
    
    def close(self):
        del self.player
        pygame.midi.quit()


if __name__ == "__main__":
    midi = Midi(0)
    
    for i in range(0, 100):
        midi.play(4, i, .05)

    midi.close()
