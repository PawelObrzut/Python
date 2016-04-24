int = raw_input('Enter file name: ')
if len(int) == 0:
    int = 'mbox-short.txt'
work = open(int)
for line in work:
    line = line.rstrip().upper()
    print line
