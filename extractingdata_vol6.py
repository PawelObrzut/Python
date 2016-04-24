#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_240489.json (Sum ends with 36)

import json
import urllib

url = raw_input('Enter location: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_240489.json'
content = urllib.urlopen(url)
data = content.read()
print 'Retriving', url
print 'Retrived', len(data),'characters'
js = json.loads(data)
print 'Count:', len(js["comments"])
sum = 0
for item in js["comments"]:
    numb = item["count"]
    numb = int(numb)
    sum = sum + numb
print 'Sum:', sum