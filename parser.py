import os
import json
from mapper import getBook

#Bible files:
f = open(os.path.join(os.getcwd(),'Bibles','english.json'))
english = json.load(f)
f.close()
f = open(os.path.join(os.getcwd(),'Bibles','hindi.json'))
hindi = json.load(f)
f.close()
f = open(os.path.join(os.getcwd(),'Bibles','telugu.json'))
telugu = json.load(f)
f.close()




def getVerse(id):
    # 00000000
    book = int(id[0:2])
    chapter = int(id[2:5])
    verse = int(id[5:8])
    bookName = getBook(id)
    engText = english['Book'][book]['Chapter'][chapter]['Verse'][verse]['Verse']
    hinText = hindi['Book'][book]['Chapter'][chapter]['Verse'][verse]['Verse']
    telText = telugu['Book'][book]['Chapter'][chapter]['Verse'][verse]['Verse']

    verseObj = {
        'book': bookName,
        'chapter': chapter+1,
        'verse': verse+1,
        'text': (engText, hinText, telText)
    }
    
    return verseObj


