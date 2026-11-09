#Wiyatt Clendenning, Module2CaseStudy.py, this program accepts a students name and checks that if their gpa qualifies for deans list or honor roll

#accepts Name and GPA
while True:
    print("enter your last name(enter ZZZ to end):")
    Lname = input()
    if Lname.upper() == "ZZZ":
       break
    print("Enter your first name: ")
    Fname = input()
    print("Enter your GPA: ")
    gpa = float(input())

    #Checks if student qualifies
    if gpa >= 3.5:
        print("Congrats " + Fname + " " + Lname + ", you qualify for the Dean's List!")
    elif gpa >= 3.25:
        print("Congrats " + Fname + " " + Lname + ", you qualify for the Honor Roll!")
    else:
        print("Sorry " + Fname + " " + Lname + ", you do not qualify.")