import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID, AGE,SALARY) \
      VALUES (1, 32, 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID, AGE,SALARY) \
      VALUES (2,  25,  15000.00 )");

conn.execute("INSERT INTO COMPANY (ID, AGE,SALARY) \
      VALUES (3,  23,  20000.00 )");

conn.execute("INSERT INTO COMPANY (ID, AGE, SALARY) \
      VALUES (4,  25,  65000.00 )");



conn.commit()
print ("Records created successfully")
conn.close()