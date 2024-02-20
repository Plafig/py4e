'''import urllib.request, urllib.parse, urllib.error
romeo = urllib.request.urlopen('https://data.pr4e.org/romeo-full.txt').read()
fhand = open('romeo-full', 'wb')
fhand.write(romeo)
fhand.close()
'''


import urllib.request, urllib.parse, urllib.error
fhand_romeo = urllib.request.urlopen('https://data.pr4e.org/romeo-full.txt')
fhand = open('romeo.txt', 'w')
for line in fhand_romeo:
    fhand.write(line.decode())
fhand.close()
fhand_read = open('romeo.txt')
print(fhand_read.read(300), "\n", len(fhand_read.read()))
fhand_read.close()