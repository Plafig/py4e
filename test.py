import urllib.request, urllib.parse, urllib.error
romeo = urllib.request.urlopen('https://data.pr4e.org/romeo-full.txt')
print(romeo.read().decode())