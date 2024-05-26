from pathlib import Path
from functools import reduce
import random

# Defining guitar notes: 

A = Path('./sound/new/Guitar_A.mp3')
B = Path('./sound/new/Guitar_B.mp3')
C = Path('./sound/new/Guitar_C.mp3')
D = Path('./sound/new/Guitar_D.mp3')
E = Path('./sound/new/Guitar_E.mp3')
F = Path('./sound/new/Guitar_F.mp3')
G = Path('./sound/new/Guitar_G.mp3')

# Making arrays for random selection or other parameters

notes = [A,B,C,D,E,F,G]
notes_ = ['A','B','C','D','E','F','G']

freq_notes = [110,123,65,73,82,87,98] # they are in alphabetical order from A-G(they are aproximate)

prefered_ratios = [{2,1}, {3,1}] # this is sort of like the answer


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
    
    print('next_note: ' + next_note)
    print('################################################')
    print('initial_note: ' + initial_note)

    iniNote_freq_ = find_item_location(notes_, initial_note)
    nextNote_freq_ = find_item_location(notes_, next_note)


    iniNote_freq = freq_notes[nextNote_freq_] # type: ignore
    nextNote_freq = freq_notes[iniNote_freq_] # type: ignore


    current_ratio = frac_simplify(iniNote_freq, nextNote_freq)
    
    for i in prefered_ratios: 
        if current_ratio == i:
            print("GOOD note FOUND")
            print(i)


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


fitness_func(random.choice(notes_), prefered_ratios, Next_note_creator())