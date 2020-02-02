import sqlite3
import datetime
from app import StudentGrade

conn= sqlite3.connect('students.db')
c= conn.cursor()

def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS studentsdb(date text,name text,address text,div text,gpa real)')
    n= int(input('enter the no of students'))
    date= datetime.datetime.now()
    dt= date.strftime("%d-%b-%Y")
    for i in range(n):
        st= StudentGrade()
        gpa= st.calculateGPA()
        c.execute("INSERT INTO studentsdb(date,name,address,div,gpa) VALUES(?, ?, ?, ?, ?)",
                  (dt,st.name,st.address,st.div,gpa))
        conn.commit()


def showData():
    c.execute('SELECT * FROM studentsdb WHERE gpa=10')
    for row in c.fetchall():
        print(row[0])


def main():
    showData()
    conn.close()
if __name__=="__main__":
    main()


