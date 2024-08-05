from pathlib import Path
from functools import reduce
import random
from pydub import AudioSegment
import pydub

# Defining guitar notes: 

A = AudioSegment.from_mp3('./sound/new/Guitar_A.mp3')
B = AudioSegment.from_mp3('./sound/new/Guitar_B.mp3')
C = AudioSegment.from_mp3('./sound/new/Guitar_C.mp3')
D = AudioSegment.from_mp3('./sound/new/Guitar_D.mp3')
E = AudioSegment.from_mp3('./sound/new/Guitar_E.mp3')
F = AudioSegment.from_mp3('./sound/new/Guitar_F.mp3')
G = AudioSegment.from_mp3('./sound/new/Guitar_G.mp3')

# Making arrays for random selection or other parameters

notes = [A,B,C,D,E,F,G]
notes_ = ['A','B','C','D','E','F','G']

freq_notes = [110,123,65,73,82,87,98] # they are in alphabetical order from A-G(they are aproximate)

prefered_ratios = [[2,1], [3,1]] # this is sort of like the answer

good_notes = []

initial_note = random.choice(notes_)

def find_item_location(list: list, item):
    x = 0
    for i in list:
        if(i == item):
            return x
        x=x+1

def Next_note_creator():
    next_note = notes_[random.randrange(0, len(notes))]
    return next_note

def fitness_func(initial_note, ratios, next_note):
    good_notes.append(initial_note)
    
    print('next_note: ' + next_note)
    print('################################################')
    print('initial_note: ' + initial_note)

    iniNote_freq_ = find_item_location(notes_, initial_note)
    nextNote_freq_ = find_item_location(notes_, next_note)


    iniNote_freq = freq_notes[nextNote_freq_] # type: ignore
    nextNote_freq = freq_notes[iniNote_freq_] # type: ignore


    current_ratio = frac_simplify(iniNote_freq, nextNote_freq)
    
    for i in prefered_ratios: 
        print('IIIIIIIIIIIIII')
        print(i)
        print('CURRENT RATIO')
        print(current_ratio)
        prefered_ratio_1_per = (float(i[0])/float(i[1]))/100 # type: ignore

        n = (float(i[0])/float(i[1])) - (float(current_ratio[0])/float(current_ratio[1])) #type: ignore

        dif = prefered_ratio_1_per * n

        print('DIFFFFFFFF')
        print(n)
        print(prefered_ratio_1_per)
        print(dif)

        if dif < 0.05:
            print("GOOD note FOUND")
            print(i)
            good_notes.append(next_note)


    print(current_ratio)


#function to find factors of a number
def factors(n):
    factors = []
    for i in range(1,round(n)+1):
        if n%i == 0:
            factors.append(i)
    return factors

#function to find the largest value in an array
def largest(arr, n):

    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

# function to simplify fractions
def frac_simplify(numerator, denominator):
    common_val = []
    large = True # True = top, False = bottom 
    largest_common_val = 0
    top = factors(float(numerator))
    bottom = factors(float(denominator))

    if len(top) > len(bottom):
        large = True
    else:
        large = False

    if (large):
        for i in top:
            if i in bottom:
                common_val.append(i)
    elif (large == False):
        for i in bottom:
            if i in top:
                common_val.append(i)

    print(top)
    print(bottom)
    
    largest_common_val = largest(common_val, len(common_val))

    print(largest_common_val)

    numerator = numerator/largest_common_val
    denominator = denominator/largest_common_val

    retur = [numerator, denominator] #* format = top number then lower number 

    return retur

def join_mp3s(good_notes, initial_note):
    sound = notes[find_item_location(notes_, initial_note)] #type:ignore
    print(sound)
    for i in range(1,len(good_notes)):
        x = (find_item_location(notes_, good_notes[i]))
        print(notes_[x]) #type:ignore
        sound = sound + notes[x] # type: ignore
        sound.export("final.mp3", format="mp3")

    print(sound.duration_seconds)

for i in range(0,len(notes_)):
    fitness_func(initial_note, prefered_ratios, Next_note_creator())

join_mp3s(good_notes, initial_note)


print(good_notes)

