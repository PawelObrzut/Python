# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    a = line.find(':')
    value = line[(a + 1):]
    value = float(value.strip())
    sum = sum + value
    xdspam = sum/count
print "Average spam confidence: ",xdspam
