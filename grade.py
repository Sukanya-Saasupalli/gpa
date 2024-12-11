def sgpa1():
    sum1 = 0
    sum2 = 0
    for i in range(len(sem1_subjects)):
        gp = int(input(f"Enter Numeric Grade in {sem1_subjects[i]} : "))
        cr = float(sem1_credits[i])
        sum1 += gp*cr
        sum2 += cr
    print(f"\nYour SGPA for Semester 1 : {round((sum1/sum2),2)}\n")

def sgpa2():
    sum1 = 0
    sum2 = 0
    for i in range(len(sem2_subjects)):
        gp = int(input(f"Enter Numeric Grade in {sem2_subjects[i]} : "))
        cr = float(sem2_credits[i])
        sum1 += gp*cr
        sum2 += cr

    print(f"\nYour SGPA for Semester 2 : {round((sum1/sum2),2)}\n")

def cgpa():
    sum1 = 0
    sum2 = 0
    for i in range(len(sem1_subjects)):
        gp = int(input(f"Enter Numeric Grade in {sem1_subjects[i]} : "))
        cr = float(sem1_credits[i])
        sum1 += gp*cr
        sum2 += cr
    for i in range(len(sem2_subjects)):
        gp = int(input(f"Enter Numeric Grade in {sem2_subjects[i]} : "))
        cr = float(sem2_credits[i])
        sum1 += gp*cr
        sum2 += cr
    
    print(f"\nYour Final CGPA : {round((sum1/sum2),2)}\n")


sem1_subjects = ["Linear Algebra and Calculus","Engineering Chemistry","Basic Electrical Engineering","Engineering Workshop","Professional English","Engineering Chemistry Lab","English Language and Communication Skills Lab","Basic Electrical Engineering Lab","Technical Seminar"]
sem1_credits = [4,4,3,2.5,2,1.5,1,1,0]

sem2_subjects = ["Advanced Calculus","Applied Physics","Programming for Problem Solving","Engineering Graphics","Applied Physics Lab","Programming for Problem Solving Lab","Environmental Science","Micro Project"]
sem2_credits = [4,4,4,3,1.5,1.5,0,0]

isok = True
print("\n\t\t\t\t\t\tGRADE CALCULATOR for B.Tech Regular I year\n")

while isok:
    select = int(input("Select Choice to calculate\n1 SGPA\n2 CGPA \nEnter Choice : "))

    if select == 1:
        choice = int(input("Select Choice\n1. SEMESTER 1\n2. SEMESTER 2\nEnter Choice : "))
        print("\n")
        if choice == 1:
            sgpa1()
        elif choice == 2:
            sgpa2()
    elif select == 2:
        cgpa()
    else:
        print("Invalid Input!!!")

    cont = int(input("Press 1 to Continue or 0 to Exit.......   "))
    if cont == 0:
        isok = False

