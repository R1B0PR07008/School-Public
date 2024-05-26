import sys
import librosa

from sound_to_midi.monophonic import wave_to_midi

print("Starting...")
file_in = './sound/guitar-single-note-d_120bpm_C_minor.mp3'

y, sr = librosa.load(file_in, sr=None)
print("Audio file loaded!")
midi = wave_to_midi(y)
print("Conversion finished!")
midi.writeFile('.mid')
print("Done. Exiting!")