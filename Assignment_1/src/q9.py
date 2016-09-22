from datetime import datetime, timedelta

def GetTime():
    sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
    d = datetime(1,1,1) + sec

    print("YEAR:MONTHS:DAYS:HOURS:MIN:SEC ")
    print("%d:%d:%d:%d:%d:%d" % (d.year-1, d.month, d.day-1, d.hour, d.minute, d.second))

GetTime()
