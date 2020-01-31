class Student:
    def __init__(self):
        self.name = input('Enter your Name: ')
        self.div = input('Enter your Branch and Section: ')
        self.regNo = input('Enter your registration number: ')
        self.address= input('Enter your address: ')
    def printInfo(self):
        print("NAME: "+self.name.upper()+'\n')
        print("DIVISION:"+self.div.upper()+'\n')
        print("regNo: "+self.regNo+'\n')

class StudentGrade(Student):
    totalCredits = 0
    courses = ["OS", "RDBMS", "MPMC", "EM4", "ELEM_FRENCH","ECO","OS_LAB","RDBMS_LAB","MPMC_LAB"]
    gradePoints = {"A+":10,"A":9,"B":8,"C":7,"D":6,"E":5,"F":4}
    course_info= {"OS":4,"RDBMS":4,"MPMC":3,"EM4":3,"ELEM_FRENCH":3,"ECO":3,"OS_LAB":1,"RDBMS_LAB":1,"MPMC_LAB":1}
    totalCredits= 23
    courseCredits = {}
    def getCourseInfo(self):
        return self.course_info

    def calculateGPA(self):
        sum = 0
        self.courseCredits = self.getCourseInfo()
        for course in self.courses:
            grade = input('Enter grade obtained in course-'+course+" ")
            if grade in self.gradePoints.keys():
                gp = self.gradePoints[grade]
                sum+= gp*self.courseCredits[course]
        gpa = sum/self.totalCredits
        return gpa
    def __init__(self):
        Student.__init__(self)

def main():
    student1 = StudentGrade()
    print("YOUR GPA IS: ",student1.calculateGPA())

if __name__== "__main__":
    main()



