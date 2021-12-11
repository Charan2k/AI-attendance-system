import sqlite3
from typing import Counter

con = sqlite3.connect('attendance-system.db')
cursor = con.cursor()
# cursor.execute('''CREATE TABLE attendance(id,rollno,date,status)''')
# cursor.execute("INSERT INTO attendance VALUES (1,501,'11-12-21','P')")
# cursor.execute("INSERT INTO attendance VALUES (2,502,'11-12-21','P')")
# cursor.execute("INSERT INTO attendance VALUES (3,503,'11-12-21','A')")
# con.commit()

cursor.execute("select * from attendance")
print(cursor)
response = cursor.fetchall()
print(cursor)
print(response)
