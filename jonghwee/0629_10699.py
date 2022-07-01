import datetime

now = datetime.datetime.now()
print( str(now + datetime.timedelta(hours=9))[:10] )