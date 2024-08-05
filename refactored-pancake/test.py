from pydub import AudioSegment

A = AudioSegment.from_mp3('./sound/new/Guitar_A.mp3')
B = AudioSegment.from_mp3('./sound/new/Guitar_B.mp3')
C = AudioSegment.from_mp3('./sound/new/Guitar_C.mp3')
D = AudioSegment.from_mp3('./sound/new/Guitar_D.mp3')
E = AudioSegment.from_mp3('./sound/new/Guitar_E.mp3')
F = AudioSegment.from_mp3('./sound/new/Guitar_F.mp3')
G = AudioSegment.from_mp3('./sound/new/Guitar_G.mp3')

A = A + B
A.export('A.mp3', format='mp3')