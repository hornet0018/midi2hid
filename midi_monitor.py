# -*- coding: utf-8 -*-
import pygame.midi

pygame.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
print("input MIDI:%d" % input_id)
i = pygame.midi.Input(input_id)

print("starting")
print("full midi_events:[[[status,data1,data2,data3],timestamp],...]")

going = True
count = 0
while going:
    if i.poll():
        midi_events = i.read(10)
        # print(midi_events)
        midi_control_channel = midi_events[0][0][1]
        midi_control_value = midi_events[0][0][2]
        if(midi_control_channel == 9):
            print(midi_control_value)
