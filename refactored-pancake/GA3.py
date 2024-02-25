from music21 import converter, instrument, note, chord
from pathlib import Path
from pitchControl import make_audios

songs = []
folder = Path('./data/sound')
for file in folder.rglob('*.wav'):
    songs.append(file)

for i,file in enumerate(songs):
    print(f'{i+1}: {file}')

make_audios('./data/sound/clean-guitar-note_A_minor.wav')