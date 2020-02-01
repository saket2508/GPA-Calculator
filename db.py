import sqlite3
from app import StudentGrade

conn= sqlite3.connect('student.db')

c= conn.cursor()

# c.execute("""CREATE TABLE students(
#            name text,
#            div text,
#            regno text,
#            address text,
#            gpa real
#            )""")

#st1= StudentGrade()
#gpa= st1.calculateGPA()
#c.execute("INSERT INTO students VALUES(?,?,?,?,?)",(st1.name,st1.div,st1.regNo,st1.address,gpa))

#conn.commit()

c.execute("SELECT * FROM students")
print(c.fetchall())

conn.close()

