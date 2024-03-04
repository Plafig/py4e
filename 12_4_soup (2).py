import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fhand_romeo = urllib.request.urlopen('https://data.pr4e.org/page1.htm')
soup = BeautifulSoup(fhand_romeo, 'html.parser')
count = 0
for p in soup.find_all('p'):
    count += 1

print(count)

