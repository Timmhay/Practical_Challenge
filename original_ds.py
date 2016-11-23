#coding=latin-1
# TURN INTO GENERATOR FUNCTION FOR 'SENTENCE' AND MAP OUT INDEX OF USEFUL INFO

import os

inputdir = "C:\\Users\\david.sheridan\\Desktop\\Temp\\Comparison"



for Datalogger in os.listdir(inputdir):
#    if os.path.isfile(Datalogger):
        Sentence = []
        Raw = open(inputdir + "\\" + Datalogger, 'br')
        IsWord = 0
        ThisWord = []
        Thischar = chr(0)
        Lastchar = chr(0)
        LS2 = chr(0)
        LS3 = chr(0)
        print("Try")
        while True:
            LS3 = LS2
            LS2 = Lastchar
            Lastchar = Thischar
            Thischar = Raw.read(1)
            if not Thischar:
                break
            if ord(LS3) == 0:
                if ord(Thischar) == 255:
                    IsWord = 1
                            
            if IsWord == 1:
                if ord(Thischar) == 255:
                    ThisWord.append(chr(255-ord(Lastchar)))

                if ord(bytes(Thischar)) == 0:
                    IsWord = 0
                    Sentence.append(''.join(ThisWord))
                    Sentence.append("\n")                   #REMOVE THIS
                    ThisWord = []
        print(''.join(Sentence))