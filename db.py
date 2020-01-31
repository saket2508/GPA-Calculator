import sqlite3
from app import StudentGrade

conn= sqlite3.connect('employees.db')

c= conn.cursor()

# c.execute("""CREATE TABLE employees(
#            name text,
#            div text,
#            regno text,
#            address text,
#            gpa real
#            )""")

#st1= StudentGrade()
#gpa= st1.calculateGPA()
#c.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(st1.name,st1.div,st1.regNo,st1.address,gpa))

#conn.commit()

c.execute("SELECT * FROM employees")
print(c.fetchall())

conn.close()

