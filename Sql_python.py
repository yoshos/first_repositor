import  mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= 'root',
    password='root',
    database="Information"
    )
##print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE INFORMATION") #this is a command

#mycursor.execute("CREATE TABLE CUSTOMERS (NAME VARCHAR(255),ADDRESS VARCHAR(255),m PHONE VARCHAR(255))")

##sql= "INSERT INTO CUSTOMERS(NAME, ADDRESS) VALUES(%s,%s)"
##val = [
##    ("Yashas", "powai"),
##    ("Yashas", "powai"),
##    ("Yashas", "powai"),
##    ]           
##mycursor.executemany(sql, val)
####val= ("YASHAS", "POWAI")
####mycursor.execute(sql,val)
##mydb.commit()
##print(mycursor.rowcount,"record inserted")

##mycursor.execute("SELECT * from CUSTOMERS")
##myresult=mycursor.fetchall()
##for i in myresult:
##    print(i)

##mycursor.execute("SELECT NAME from CUSTOMERS")
##myresult=mycursor.fetchall()
##for i in myresult:
##    print(i)

##sql = "Select * from customers where address='Powai'"
##mycursor.execute(sql)
##myresult=mycursor.fetchall()
##for i in myresult:
##    print(i)

##sql = "UPDATE customers set address= 'Andheri' where address= 'Powai'"
##mycursor.execute(sql)
##mydb.commit()
##print(mycursor.rowcount,"record update")

##mycursor.execute("SELECT * from customers limit 2")
##myresult= mycursor.fetchall()
##for i in myresult:
##    print (i)
##mycursor.execute("SELECT * from customers limit 1 offset 2")
##a=mycursor.fetchall()
##for i in a:
##    print(i)

##sql= "DELETE From Customers where address= 'Andheri'"
##
##myresult= mycursor.execute(sql)
##mydb.commit()

mycursor=mydb.cursor()
sql= "drop table customers"
mycursor.execute(sql)





