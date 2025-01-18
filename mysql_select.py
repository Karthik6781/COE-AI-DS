import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur=mydb.cursor()
cur.execute("select * from employee")
std=cur.fetchall();
for i in std:
    print(i)
cur.execute("select * from employee order by ename;")
std=cur.fetchall();
for i in std:
    print(i)
cur.execute("select * from employee where salary between 75000 and 80000;")
std=cur.fetchall();
for i in std:
    print(i)
mydb.commit()