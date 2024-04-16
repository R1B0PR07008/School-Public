from music21 import converter, instrument, note, chord
from pathlib import Path
from pitchControl import make_audios
import random

songs = []
folder = Path('./')
for file in folder.rglob('*.mp3'):
    songs.append(file)

result =  random.sample([x for x in songs], min(20, len(songs)))

for i,file in enumerate(songs):
    print(f'{i+1}: {file}')

notes = []
for i,file in enumerate(result):
    print(f'{i+1}: {file}')

