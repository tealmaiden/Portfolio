import datetime
from datetime import datetime
from pytz import timezone

##Finding Time Zones:

##from pytz import all_timezones
##print len(all_timezones)
##for zone in all_timezones:
##    if 'Europe' in zone:
##        print zone

##US/Pacific
##US/Eastern
##Europe/London

time = "%H:%M:%S"
regtime = "%I:%M%p"
#time style: year, month, day, hour minute, second, time zone

# Current time in Portland
now_portland = datetime.now(timezone('US/Pacific'))
np = now_portland.strftime(time)
npreg = now_portland.strftime(regtime)
print 'Portland time: ', npreg

# Convert to US/Eastern time zone
now_newYork = now_portland.astimezone(timezone('US/Eastern'))
ny = now_newYork.strftime(time)
nyreg = now_newYork.strftime(regtime)
print 'New York time: ', nyreg

# Convert to Europe/London time zone
now_london = now_portland.astimezone(timezone('Europe/London'))
nl = now_london.strftime(time)
nlreg = now_london.strftime(regtime)
print 'London time: ', nlreg

##32400=open time
##75600=closed time

#With datetime:
#Portland, New York, London Conversion (np, ny, nl):
[hours, minutes, seconds] = [int(x) for x in np.split(':')]
npsec=hours*3600+minutes*60+seconds

[hours, minutes, seconds] = [int(x) for x in ny.split(':')]
nysec=hours*3600+minutes*60+seconds

[hours, minutes, seconds] = [int(x) for x in nl.split(':')]
nlsec=hours*3600+minutes*60+seconds

##another way:
##x = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
##npsec = x.seconds

#Message:
if 32400<=npsec<=75600:
    print 'Portland store is open'
else:
    print 'Portland store is closed'

if 32400<=nysec<=75600:
    print 'New York store is open'
else:
    print 'New York store is closed'

if 32400<=nlsec<=75600:
    print 'London store is open'
else:
    print 'London store is closed'


