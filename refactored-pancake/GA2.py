from music21 import converter, instrument, note, chord
from pathlib import Path
# import pyaudio
import random
import struct
import math

good_pairs = []
user_feedback = []
notes_filtered = []
frequencies = []
prefered_ratios = []

# p = pyaudio.PyAudio()
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
RATE = 44100

def data_for_freq(frequency: float, time: float):
    """get frames for a fixed frequency for a specified time or
    number of frames, if frame_count is specified, the specified
    time is ignored"""
    frame_count = int(RATE * time)

    remainder_frames = frame_count % RATE
    wavedata = []

    for i in range(frame_count):
        a = RATE / frequency  # number of frames per wave
        b = i / a
        c = b * (2 * math.pi)
        d = math.sin(c) * 32767
        e = int(d)
        wavedata.append(e)

    for i in range(remainder_frames):
        wavedata.append(0)

    number_of_bytes = str(len(wavedata))  
    wavedata = struct.pack(number_of_bytes + 'h', *wavedata)

    return wavedata

# def play(frequency: float, time: float):
#     """
#     play a frequency for a fixed time!
#     """
#     frames = data_for_freq(frequency, time)
#     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
#     stream.write(frames)
#     stream.stop_stream()
#     stream.close()

def removefromarray(note):
    for i in range(1,7):
        try:
            istr = str(i)
            index = note+'-'+istr+''
            notes_filtered.remove( index)
        except:
            pass

songs = []
folder = Path('/home/r1b0ld1/Documents/GitHub/School-Public/refactored-pancake/data/archive')
for file in folder.rglob('*.mid'):
    songs.append(file)

# Get a subset of 1000 songs
result =  random.sample([x for x in songs], min(100, len(songs)))

notes = []
for i,file in enumerate(result):
    print(f'{i+1}: {file}')
    try:
      midi = converter.parse(file)
      notes_to_parse = None
      parts = instrument.partitionByInstrument(midi)
      if parts: # file has instrument parts
          notes_to_parse = parts.parts[0].recurse() # type: ignore
      else: # file has notes in a flat structure
          notes_to_parse = midi.flat.notes
      for element in notes_to_parse:
          if isinstance(element, note.Note):
              notes.append(str(element.pitch))
          elif isinstance(element, chord.Chord):
              pass
    except:
      print(f'FAILED: {i+1}: {file}')
  
for i in notes:

    if i not in notes_filtered:

        notes_filtered.append(i)

removefromarray('E')
removefromarray('B')
removefromarray('C')

print("")
print("################################################################")
print("final/filtered notes:")
print(notes_filtered)

#** finding pairs of good sounding notes

cF = ['16.35', '32.70', '65.41',	'130.81', '261.63',	'523.25', '1046.50', '2093.00',	'4186.01']
Cs_DbF = ['17.32', '34.65',	'69.30', '138.59', '277.18', '554.37', '1108.73', '2217.46', '4434.92']
dF = ['18.35', '36.71', '73.42', '146.83', '293.66', '587.33', '1174.66', '2349.32', '4698.63']
Ds_EbF = ['19.45', '38.89', '77.78', '155.56', '311.13', '622.25', '1244.51', '2489.02', '4978.03 ']
eF = ['20.60', '41.20', '82.41', '164.81', '329.63', '659.25','1318.51', '2637.02', '5274.04 ']
fF = ['21.83', '43.65', '87.31', '174.61', '349.23', '698.46', '1396.91', '2793.83', '5587.65 ']
Fs_GbF = ['23.12', '46.25', '92.50', '185.00', '369.99', '739.99', '1479.98', '2959.9', '5919.91 ']
gF = ['24.50', '49.00', '98.00', '196.00', '392.00', '783.99', '1567.98', '3135.96', '6271.93 ']
Gs_AbF = ['25.96', '51.91', '103.83', '207.65', '415.30', '830.61', '1661.22', '3322.44', '6644.88 ']
aF = ['27.50', '55.00', '110.00', '220.00', '440.00', '880.00', '1760.00', '3520.00', '7040.00 ']
As_BbF = ['29.14', '58.27', '116.54', '233.08', '466.16', '932.33', '1864.66', '3729.31', '7458.62 ']
bF = ['30.87', '61.74', '123.47', '246.94', '493.88', '987.77', '1975.53', '3951.07', '7902.13 ']

notes_frecquencies = ['cF', 'Cs_DbF', 'dF', 'Ds_EbF', 'eF', 'fF', 'Fs_GbF', 'gF', 'Gs_AbF', 'aF', 'As_BbF', 'bF']

prefered_ratios = [2/1, 3/1] # this is sort of like the answer
#, 4/1

notes_frecquencies = []

final_notes = []

good_notes = []

def notes_to_frequency(note):
    lenNote = len(note)
    octave = 0
    if lenNote == 3:
        octave = int(note[2])-1
        note_1 = note[0]
        note_0 = note[1]
        note_ = note_1+note_0
    else:
        octave = int(note[1])-1
        note_ = note[0]

    if note_ == 'C':
        return float(cF[int(octave)])
    elif note_ == 'C#':
        return float(Cs_DbF[int(octave)])
    elif note_ == 'D':
        return float(dF[int(octave)])
    elif note_ == 'D#':
        return float(Ds_EbF[int(octave)])
    elif note_ == 'E':
        return float(eF[int(octave)])
    elif note_ == 'F':
        return float(fF[int(octave)])
    elif note_ == 'F#':
        return float(Fs_GbF[int(octave)])
    elif note_ == 'G':
        return float(gF[int(octave)])
    elif note_ == 'G#':
        return float(Gs_AbF[int(octave)])
    elif note_ == 'A':
        return float(aF[int(octave)])
    elif note_ == 'A#':
        return float(As_BbF[int(octave)])
    elif note_ == 'B':
        return float(bF[int(octave)])

def notes_to_frequencyfunc():
    for i in notes_filtered:

        if i not in notes_frecquencies:

            notes_frecquencies.append(notes_to_frequency(i))

    return notes_frecquencies

notes_frecquencies_ = (notes_to_frequencyfunc())

def finess_func_ini(initial_note, ratios):
    ini_note = notes_to_frequency(initial_note)
    final_notes.append(ini_note)
    print(ini_note)
    print(final_notes)
    print(notes_frecquencies)
    print(notes_filtered)
    for i in notes_frecquencies_: # type: ignore
        divi = round(i/ini_note)
        print(divi)
        note_freq = i # type: ignore
        for i in ratios:
            if divi == i:
                # print("GOOD NOTES!!!")
                # print("divi")
                # print(divi)
                # print("note:")
                # print(note_freq)
                # print("ratios")
                # print(i)
                # print('')
                good_notes.append(note_freq)
    print(len(good_notes))
    print(good_notes)
    previous_note = good_notes[random.randrange(0, len(good_notes))]
    for i in range(0,len(good_notes)):
        if good_notes[i] != previous_note:
            final_notes.append(good_notes[i])
            final_notes.append(good_notes[i+1])
            break
    final_notes.append(previous_note)
    return previous_note

def fitness_func(ini_note, ratios):
    good_notes = []
    previous_note = finess_func_ini(ini_note,ratios)
    for i in range(1, 3):
        for i in notes_frecquencies:
            divi = round(i/previous_note)
            note_freq = i
            for i in ratios:
                if divi == i:
                    good_notes.append(note_freq)
        print("good notes:")
        print(good_notes)
        previous_note = good_notes[random.randrange(1,len(good_notes))]
        for i in range(0,len(good_notes)):
            if good_notes[i] != previous_note:
                final_notes.append(good_notes[i])
                final_notes.append(good_notes[i+1])
                break
        final_notes.append(previous_note)
        good_notes = []


#* deciding how long a note plays for

bpm = [60, 100, 30, 200]

# placement works like this: place,type of note
# 1= whole, 2=half, 4=quater, 8=eight
notes_ = ['1','2','4','8']

m = []
for i in range(1,9):
    if i >= 2:
        m.append('p'+str(i)+','+notes_[random.randrange(1,4)])
    else:
        m.append('p'+str(i)+','+notes_[random.randrange(0,4)])

# current fav measure ['p1,2', 'p2,8', 'p3,8', 'p4,2', 'p5,8', 'p6,2', 'p7,4', 'p8,2']

def bpmToS(bpm, measure):
    pass
    # change the measure/bmp to the amount of seconds a note has to play.
    S = float(bpm)/60
    if measure[3] == '1':
        S = S*4
        return S
    elif measure[3] == '2':
        S = S*2
        return S
    elif measure[3] == '4':
        S = S
        return S
    elif measure[3] == '8':
        S = S/2
        return S

def timesPlayed(measure):
    TP = 0
    if measure[3] == '1':  # type: ignore
        TP = 9
    elif measure[3] == '2':  # type: ignore
        TP = 3
    elif measure[3] == '4':  # type: ignore
        TP = 1
    elif measure[3] == '8':  # type: ignore
        TP = 2
    return TP

# def timings(measures, bpm, final_notes):
#     BPM = bpm[random.randrange(0,3)]
#     BPMt = BPM/60
#     M = measures
#     c = 0
#     print(M)
#     for i in final_notes:
#         print("frequency: ")
#         print(float(i))
#         print("time")
#         print(float(bpmToS(BPM, M[c]))) # type: ignore
#         play(float(i), float(bpmToS(BPM, M[c]))) # type: ignore
#         if timesPlayed(M[c]) == 9: # type: ignore
#             break
#         elif timesPlayed(M[c]) == 3:
#             if c == 1:
#                 break
#         elif timesPlayed(M[c]) == 1:
#             pass
#         elif timesPlayed(M[c]) == 2:
#             play(float(i), float(bpmToS(int(BPM), M[c]))) # type: ignore

#         if c == 6 and timesPlayed(M[c]) != 2:
#             break
#         elif c == 7:
#             break
#         c = c+1

print("################################################################")
print("finess_func_ini: ")
fitness_func('D3', prefered_ratios)
print("################################################################")
print("final notes: ")
print(final_notes)
print("################################################################")
print("good notes: ")
print(good_notes)
print("################################################################")
print("timings")
# timings(m, bpm, final_notes)
