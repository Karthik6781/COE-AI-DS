import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur=mydb.cursor()
name=input("Enter your name:")
id=input("Enter your id:")
cur.execute("update student set sname=%s where sid=%s",(name,id))
print("table updated")
mydb.commit()