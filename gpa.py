class student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.id = input("Enter your student id: ")
        self.address = input("Enter your address: ")
        self.div = input("Enter your division: ")
    def printstudentInfo(self):
        print("WELCOME " + self.name.upper())
        print("Your student id is: " + self.id)
        print("Your address is : " + self.address)
        print("Your division is: " + self.div)

class studentgrades(student):
    def __init__(self):
        student.__init__(self)
        self.courses = ["EM3","OOP_java","CompArch","Lab","ValuesEthics","DS","LogicDesign"]
        self.course_data = dict.fromkeys(self.courses)
        for course in self.course_data:
            print("course: " + course)
            val = input("Enter your grade and credits: ").split(" ")
            self.course_data[course] = val
    def GPAcalc(self):
        print(self.course_data)
        gp = {"A+":10,"A":9,"B":8,"C":7,"D":6,"E":5,"F":4}

        for pt in self.course_data.values():
            if pt[0] in gp:
                pt[0] = gp[pt[0]]
        gpsum = 0
        creditsum = 0
        for pt in self.course_data.values():
            gpsum+= pt[0]*(int(pt[1]))
        for pt in self.course_data.values():
            creditsum+= int(pt[1])
        self.gpa = gpsum/creditsum
        print("your gpa is: %.2f" % self.gpa)
        for course,grades in self.course_data.items():
            if(grades[0]==4):
               flag = 0
               print("Sorry, you have failed. You may have to take a retest in order to pass.")
               break
            else:
                flag = 1
        if(flag==1): print("Congratulations! You have passed.")
st1 = studentgrades()
st1.printstudentInfo()
st1.GPAcalc()

