#The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_240488.html (Sum ends with 7)

#import library
import urllib
from BeautifulSoup import *

#get url
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
count = 0
sum = 0

for tag in tags:
    count = count + 1
    num = tag.contents[0]
    num = int(num)
    sum = sum + num

print 'Count',count
print 'Sum', sum