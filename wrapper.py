from generator import *
from parser import *
from datetime import date
import os
import json

#_date = date.today()
#_today = str(_date.year) + "-" + str(_date.month) + "-" + str(_date.day)

_today = '2021-02-25'
f = open(os.path.join(os.getcwd(),'calendar-data-21-f-d.json'))
dates = json.load(f)
f.close()


verseID = dates['Hebron'][_today]['verseid']
verseObj = getVerse(verseID)
modify_html(verseObj)
convert_to_image(verseObj)
