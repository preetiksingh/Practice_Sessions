import urllib
u=urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data=u.read()
print data
f=open('ab22.xml','wb')
f.write(str(data))
f.close
daves_latitude=41.98062

from xml.etree.ElementTree import parse
doc=parse('ab22.xml')
for bus in doc.findall('bus'):
    lat=float(bus.findtext('lat'))
    if lat > daves_latitude:
        direction=bus.findtext('d')
        if direction.startswith('North'):
            busid=bus.findtext('id')
            print busid,lat


