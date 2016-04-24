#fname = raw_input("Enter file name: ")
fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for word in line:
        word = word.split()
        app = word[0]
        if app in lst : continue
        else:
            lst.append(app)
lst.sort()
print lst
    

#print line.rstrip()


