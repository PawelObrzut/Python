#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

#Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
#Last name in sequence: Anayah
#Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Dilya.html 
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: P


#Import Biblioteki
import urllib
from BeautifulSoup import *

#Adres zrodla
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Wartosci uzytkownika
position = raw_input('Enter position: ')
position = int(position)
repeat = raw_input('Enter count: ')
repeat = int(repeat)

print url

while repeat > 0:
    repeat = (repeat - 1)
    #zasoby
    list = {}
    count = 0
    tags = soup('a')
    tmp = []

    #Tworzenie katalogu adresow
    for tag in tags:
        href = tag.get('href', None)
        count = count + 1
        list[href] = list.get(href,count)

    #Porzadkowanie katalogu. Pozyskanie adresu
    for k,v in list.items():
        tmp.append((v,k))
    tmp.sort()
    for v,k in tmp[(position - 1):position]:
        url = k
        print 'Retrieving:', url
    
    #Podazanie za linkiem
    url = k
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
