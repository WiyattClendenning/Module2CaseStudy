#Wiyatt Clendenning, Module2CaseStudy.py, this program accepts a students name and checks that if their gpa qualifies for deans list or honor roll

#accepts Name and GPA
print("Enter your name: ")
name = input()
print("Enter your GPA: ")
gpa = float(input())
print(gpa)

#Checks if student qualifies
if gpa >= 3.5:
    print("Congrats " + name + "you qualify for the Dean's List!")
elif gpa >= 3.25:
    print("Congrats " + name + ", you qualify for the Honor Roll!")
else:
    print("Sorry " + name + ", you do not qualify.")