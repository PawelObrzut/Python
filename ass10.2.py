#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"

name = 'mbox-short.txt'
handle = open(name)
count = 0
dict = {}

for line in handle:
    if line.startswith('From: '):continue
    elif line.startswith('From'):
        count = count + 1
        line = line.split()
        time = line[5]
        time = time.split(':')
        hour = time[0]
        dict[hour] = dict.get(hour,0) + 1

for k in sorted(dict):
    print k, dict[k]   
