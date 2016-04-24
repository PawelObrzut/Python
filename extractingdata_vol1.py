#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#We provide two files for this assignment. 
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 87 values with a sum=445822)
#Actual data: http://python-data.dr-chuck.net/regex_sum_240483.txt (There are 86 values and the sum ends with 466)

source = open('actualdata.txt')
import re
numbers = list()
cyfry = list()

for line in source:
    num = re.findall('[0-9]+',line)
    #print num
    if num is None : continue
    if len(num) == 0 : continue
    else:
        numbers.extend(num)

for element in numbers:
    element = int(element)
    cyfry.append(element)

print sum(cyfry)