import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur=mydb.cursor()
cur.execute("create table employee(eid int, ename varchar(20), city varchar(20), salary int)")
print("table created")
mydb.commit()