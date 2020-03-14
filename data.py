import mysql.connector as mysql
conn=mysql.connect(user="root" ,password="scott" ,host="127.0.0.1")
c=conn.cursor()
c.execute("use python1")
c.execute("select * from employee")
rows=c.fetchall()
id=row[1][0]
print(id)
c.execute("update employee.set name='pqr' where eno="+str(id))
id=input("enter employee id to delete")
c.execute("delete from employee where eno="+str(empid))
