from music21 import converter, instrument, note, chord
from pathlib import Path

songs = []
folder = Path('/home/r1b0ld1/Documents/GitHub/School-Public/refactored-pancake/data/sound')
for file in folder.rglob('*.wav'):
    songs.append(file)

for i,file in enumerate(songs):
    print(f'{i+1}: {file}')
