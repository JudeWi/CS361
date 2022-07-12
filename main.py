from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import time
import numpy as np

def del_chord(index, chords):
    print("Would you like to delete the contents of this chord? (y/n)")
    y_n = input()
    if y_n == "y":
        for n in range(4):
            chords[index, n] = 0


def defa_chord(index, chords, sines):
    return

def edit_notes(index, chords, sines):
    truth = 1
    while(truth):
        print("Which note would you like to edit? (1-4)")
        val = int(input())
        if val > 0 and val < 5:
            print("Pick a new note: (1-14)")
            print("C = 1, D = 2, etc...")
            note = int(input())
            if note > 0 and note < 15:
                chords[index, (val - 1)] = sines[(note - 1)]
                print("Would you like to edit another note? (y/n)")
                val = input()
                if val == "y":
                    continue
                else:
                    truth = 0
            else:
                print("Invalid input... Try again.")
        else:
            print("Invalid input... Try again.")
    return

def edit_chord(index, chords, sines):
    truth = 1
    while(truth):
        print("Selected chord:")
        disp_chord(index, chords, sines)
        print("What would you like to do with the chord?")
        print("1: Play")
        print("2: Edit notes")
        print("3: Change chord")
        print("4: Delete")
        print("5: Exit")
        val = input()
        if val == "1":
            play_chords(index, chords)
        elif val == "2":
            edit_notes(index, chords, sines)
        elif val == "3":
            defa_chord(index, chords, sines)
        elif val == "4":
            del_chord(index, chords)
        elif val == "5":
            truth = 0
        else:
            print("Invalid entry... Try again")

def edit_func(chords, sines):
    ex = 1
    while(ex):
        print("Which chord would you like to edit? (1-8)")
        val = int(input())
        if val < 9 and val > 0:
            edit_chord((val - 1), chords, sines)
            print("Would you like to edit another chord? (y/n)")
            y_n = input()
            if y_n == "y":
                continue
            elif y_n == "n":
                ex = 0
        else:
            print("Invalid entry... Try again.")
    

def create_overlay(index, chords, ready_chords = None):
    if ready_chords is None:
        temp_chord = Sine(0).to_audio_segment(duration = 700)
        for n in range(4):
            if chords[index, n] != 0:
                temp_chord = temp_chord.overlay(chords[index, n])
        play(temp_chord)
    else:
        ready_chords[index] = Sine(0).to_audio_segment(duration = 700)
        for n in range(4):
            if chords[index, n] != 0:
                ready_chords[index] = ready_chords[index].overlay(chords[index, n])
    return

def play_chords(index, chords, ready_chords = None):
    if index == -1:
        for c in range(8):
            create_overlay(c, chords, ready_chords)
        for c in range(8):
            play(ready_chords[c])
    elif ready_chords is None:
        create_overlay(index, chords, None)
    return

def disp_chord(index, chords, sines):
    print("%.0f |-" % (index + 1), end='')
    for n in range(4):
        if chords[index, n] == sines[0]:
            print("-C--", end='')
        elif chords[index, n] == sines[1]:
            print("-D--", end='')
        elif chords[index, n] == sines[2]:
            print("-E--", end='')
        elif chords[index, n] == sines[3]:
            print("-F--", end='')
        elif chords[index, n] == sines[4]:
            print("-G--", end='')
        elif chords[index, n] == sines[5]:
            print("-A--", end='')
        elif chords[index, n] == sines[6]:
            print("-B--", end='')
        elif chords[index, n] == sines[7]:
            print("-C2-", end='')
        elif chords[index, n] == sines[8]:
            print("-D2-", end='')
        elif chords[index, n] == sines[9]:
            print("-E2-", end='')
        elif chords[index, n] == sines[10]:
            print("-F2-", end='')
        elif chords[index, n] == sines[11]:
            print("-G2-", end='')
        elif chords[index, n] == sines[12]:
            print("-A2-", end='')
        elif chords[index, n] == sines[13]:
            print("-B2-", end='')
        else:
            print("----", end='')
    print("|")

def disp_chords(chords, sines):
    print("Your current chords:")
    print("  |--1---2---3---4--|")
    #Formatting: print("  |--C---A---F---G--|")
    for c in range(8):
        disp_chord(c, chords, sines)
        print("  |-----------------|")



def menu_func(sines, chords, ready_chords, def_chords):
    truth = 1
    while(truth):
        disp_chords(chords, sines)
        print("What would you like to do?")
        print("1: Play")
        print("2: Edit")
        print("3: Save")
        print("4: Exit")
        val = input()
        if val == "1":
            play_chords(-1, chords, ready_chords)
        elif val == "2":
            edit_func(chords, sines)
        elif val == "3":
            print("This hasn't been incorporated yet!")
        elif val == "4":
            truth = 0
        else:
            print("Invalid input... Try again")


def startup(sines, chords, def_chords):
    print("Loading notes...")
    t = time.time()
    C_note = Sine(261.63)
    D_note = Sine(293.66)
    E_note = Sine(329.63)
    F_note = Sine(349.23)
    G_note = Sine(392)
    A_note = Sine(440)
    B_note = Sine(493.88)
    C2_note = Sine(523.25)
    D2_note = Sine(587.33)
    E2_note = Sine(659.25)
    F2_note = Sine(698.46)
    G2_note = Sine(783.99) 
    A2_note = Sine(880)
    B2_note = Sine(987.77)
    elapsed = time.time() - t
    print("Notes loaded in %.3f seconds!" % elapsed)

    print("Loading sounds...")
    t = time.time()
    sines[0] = C_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[1] = D_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[2] = E_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[3] = F_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[4] = G_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[5] = A_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[6] = B_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[7] = C2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[8] = D2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[9] = E2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[10] = F2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[11] = G2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[12] = A2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    sines[13] = B2_note.to_audio_segment(duration=500).fade_in(100).fade_out(300)
    elapsed = time.time() - t
    print("Sounds loaded in %.3f seconds!" % elapsed)

    print("Loading default chords...")
    t = time.time()
    def_chords[0] = sines[0].overlay(sines[2]).overlay(sines[4])     #I      (Cmaj)
    def_chords[1] = sines[1].overlay(sines[3]).overlay(sines[5])     #ii     (Dmin)
    def_chords[2] = sines[2].overlay(sines[4]).overlay(sines[6])     #iii    (Emin)
    def_chords[3] = sines[3].overlay(sines[5]).overlay(sines[7])     #IV     (Fmaj)
    def_chords[4] = sines[4].overlay(sines[6]).overlay(sines[8])     #V      (Gmaj)
    def_chords[5] = sines[5].overlay(sines[7]).overlay(sines[9])     #vi     (Amin)
    def_chords[6] = sines[6].overlay(sines[8]).overlay(sines[10])    #vii^   (Bdim)
    
    chords[0,0] = sines[0]
    chords[0,1] = sines[2]
    chords[0,2] = sines[4]
    chords[1,0] = sines[4]
    chords[1,1] = sines[6]
    chords[1,2] = sines[8]
    chords[2,0] = sines[5]
    chords[2,1] = sines[7]
    chords[2,2] = sines[9]
    chords[3,0] = sines[6]
    chords[3,1] = sines[8]
    chords[3,2] = sines[10]

    elapsed = time.time() - t
    print("Chords loaded in %.3f seconds!" % elapsed)

sines = np.zeros([14], dtype = object)
chords = np.zeros([8, 4], dtype = object)
ready_chords = np.zeros([8], dtype = object)
for n in range(8):
    ready_chords[n] = Sine(0).to_audio_segment(duration = 700)
def_chords = np.zeros([7], dtype = object)
startup(sines, chords, def_chords)
print("Welcome to the chord progression generator!")
print("This tools allows users to generate chords with up to 4 note polyphony,")
print("and up to 8 chords in any one progression.")
print("To begin we've started you with the classic I-V-vi-IV chord progression.")
menu_func(sines, chords, ready_chords, def_chords)


