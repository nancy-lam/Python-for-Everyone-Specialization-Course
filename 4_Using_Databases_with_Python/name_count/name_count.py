#Counting senders
#This application will read the mbox-short.txt
#and count the number of senders
#using a database with the following schema to maintain the counts.

#The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

#Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, 
# it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.


import sqlite3

conn = sqlite3.connect('namedb.sqlite')
cur = conn.cursor()

# Create table

cur.executescript('''
DROP TABLE IF EXISTS Counts;
                  
CREATE TABLE Counts (
                  name  TEXT,
                  count INTEGER);
''')

# Prompt for file name

file_name = input('Enter file name: ')
if (len(file_name) < 1):
    file_name = 'mbox-short.txt'

file = open(file_name)
for line in file:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    name = email.split('@')[0]
    
    cur.execute('SELECT count FROM Counts WHERE name = ?', (name, ))
    row = cur.fetchone()

    if row is None: 
        cur.execute('INSERT OR IGNORE INTO Counts (name, count) VALUES (?, 1)', (name,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE name = ?', (name, ))
    conn.commit()
    
sqlstr = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0], str(row[1]))

cur.close()