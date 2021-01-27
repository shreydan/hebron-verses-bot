import json
import os
import datetime

from datetime import date, timedelta

dates = {}
# commented coz running this
# will reset the json file
"""
sdate = date(2021, 2, 1)   # start date
edate = date(2021, 12, 31)   # end date
delta = edate - sdate       # as timedelta
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    dates[str(day)] = {'verseid': ''}

with open('calendar-data-21-f-d.json','w+') as f:
    f.write(json.dumps({"Hebron": dates},indent=4))
f.close()
"""