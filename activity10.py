#python demi for nested condition
#Data filtration program

name = input("Enter your name :")
aStudent = input("Are you a current student of DLL this year? (Yes/No) :  ")

if aStudent.lower() == "yes" :
    YearLev = input("What year you are currently enrolled? \nF - freshman \nS - Sophomore\nJ - Junior\nSn - Senior\n\nPlease input your answer here:  ")


    if YearLev. lower () == "f":
        print(f"Hi Good day!{name} , Freshman , Welcome to DLL ")
    elif YearLev. lower() == "s":
        print(f"Hi Good day!{name} , Sophomore, Welcome to DLL ")
    if YearLev. lower () == "j":
        print(f"Hi Good day!{name} , Junior, Welcome to DLL ")
    if YearLev. lower () == "sn":
         print (f"Hi Good day!{name}, Senior, Welcome to DLL ")
else:
    print("Thank you for using the system ")