#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#We provide two files for this assignment. 
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 87 values with a sum=445822)
#Actual data: http://python-data.dr-chuck.net/regex_sum_240483.txt (There are 86 values and the sum ends with 466)

import re
print sum( [ int(all) for all in re.findall('[0-9]+', open('actualdata.txt').read()) ] )
