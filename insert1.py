import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur=mydb.cursor()
n=int(input("Enter no.of employees:"))
for i in range(n):
    name = input("Enter your name:")
    id = input("Enter your id:")
    city=input("Enter your city :")
    salary=input("Enter your salary :")
    cur.execute("insert into employee values(%s,%s,%s,%s)", (id, name, city, salary))
    mydb.commit()
print("Records inserted")
