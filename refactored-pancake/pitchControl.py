from pydub import AudioSegment
import numpy as np
fileName = '/home/r1b0ld1/Documents/GitHub/School-Public/refactored-pancake/sound/guitar-single-note-d_120bpm_C_minor.mp3'
sound  = AudioSegment.from_file(fileName, format='mp3')

def make_audios(file):
    filename = file
    sound = AudioSegment.from_file(fileName, format='mp3')

    octaves = 0.5
    one_second = 2 *1000

    for octaves in np.linspace(-1,1,21):
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        hipitch_sound = hipitch_sound.set_frame_rate(44100)
    #export / save pitch changed sound
        hipitch_sound_out = hipitch_sound[:one_second]
        hipitch_sound_out.export(f"octave_{octaves}.mp3", format="mp3")

make_audios(sound)
# hipitch_sound = hipitch_sound.set_frame_rate(44100) #sets a frame rate

# hipitch_sound.export("out.wav", format="wav") # exports the sound as wav
