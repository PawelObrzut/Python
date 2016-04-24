import sqlite3

bridge = sqlite3.connect('sqlite.sqlite')
connection = bridge.cursor()

connection.execute('''DROP TABLE IF EXISTS Counts''')
connection.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox.txt'
fhandle = open(fname)

for line in fhandle:
    if not line.startswith('From: '): continue
    elements = line.split()
    email = elements[1]
    domain = email.split('@')
    org = domain[1]
    connection.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
    try:
        count = connection.fetchone()[0]
        connection.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
    except:
        connection.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org, ))
    bridge.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in connection.execute(sqlstr):
     print str(row[0]), row[1]

bridge.close()   