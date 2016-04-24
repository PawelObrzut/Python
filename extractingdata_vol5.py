#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_240485.xml (Sum ends with 36)

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_42.xml'
content = urllib.urlopen(url)
data = content.read()
print 'Retrieving', url
print 'Retrived', len(data), 'characters'


tree = ET.fromstring(data)
lst = tree.findall('.//count')
print data
sum = 0

for value in lst:
    x = value.text
    x = int(x)
    sum = sum + x

print 'Count: ',len(lst)
print 'Sum: ', sum