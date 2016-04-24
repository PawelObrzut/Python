#Read the file and print in capital letters all lines
inp = raw_input('Enter file name: ') + ('.txt')
file = open(inp)
go_on = file.read()
go_on = go_on.rstrip()
print go_on.upper()