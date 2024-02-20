import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fhand_romeo = urllib.request.urlopen('https://data.pr4e.org/romeo-full.txt')
soup = BeautifulSoup(fhand_romeo, 'html.parser')
print("Debug: ", soup)