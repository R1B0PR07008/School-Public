from pydub import AudioSegment
fileName = '/home/r1b0ld1/Documents/GitHub/School-Public/refactored-pancake/sound/guitar-single-note-d_120bpm_C_minor.mp3'
sound  = AudioSegment.from_file(fileName, format='wav')

octaves = 1

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves)) # changes sample rate 

hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}) # applies new sample rate

hipitch_sound = hipitch_sound.set_frame_rate(44100) #sets a frame rate

hipitch_sound.export("out.wav", format="wav") # exports the sound as wav
