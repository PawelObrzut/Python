fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From:'):continue
    elif line.startswith('From'):
        count = count + 1
        linecontent = line.split()
        print linecontent[1]
    else: continue

print "There were", count, "lines in the file with From as the first word"