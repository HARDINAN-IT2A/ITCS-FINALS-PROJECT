isContinue = True
def activity1():
    print("Hello world!")

def activity2():
    num1 = eval(input("Please enter a number:  "))
    num2 = eval(input("Please enter another number:  "))
    print(f"{num1} Floor divided to {num2} = {num1 // num2}")

def activity3():
    positionDs = input("What position you're applying for? ")
    date = input("Date today: ")
    yourName = input("Enter your full name: ")
    presentAdd = input("Enter your present address: ")
    permanentAdd = input("Enter your permanent address: ")
    mobileNo = input("Enter your mobile number: ")
    homeNo = input("Enter home number: ")
    dateBirth = input("Enter your birthday: ")
    placeBirth = input("Enter the place of your birth: ")
    citizenship = input("Enter your nationality: ")
    religion = input("Enter your religion: ")
    yAge = input("Enter your age: ")
    ySex = input("Enter your sex: ")
    civilStat = input("Enter your civil status: ")
    yHeight = input("Enter your height: ")
    yWeight = input("Enter your weight: ")
    spouseN = input("Enter the name of your spouse: ")
    occup = input("Enter your occupation: ")
    noChild = input("Enter the number of your children: ")
    namesAbirth = input("Enter their names and birthday: ")
    fatherN = input("Enter the name of your father: ")
    fOccup = input("Enter your father's occupation: ")
    fAdd = input("Enter the adress of your father: ")
    motherN = input("Enter the name of your mother: ")
    mOccup = input("Enter your mother's occupation: ")
    mAdd = input("Enter the address of your mother: ")
    language = input("Enter the langauges or dialects you can speak: ")
    pEmergency = input("Who's the person to be contacted in case of emergency? ")
    relation = input("What is your relationship with him or her?" )
    pAdd= input("His/her address: ")
    pTel = input("His/her telephone number: ")
    elem = input("Name of your elementary school: ")
    deg = input("What degree you received? ")
    year = input("What year you graduated? ")
    highscl = input("Name of your high school: ")
    dEg = input("What degree you received? ")
    yEar = input("What year you graduated? ")
    collg = input("Name of your college school: ")
    deG = input("What degree you received? ")
    yeAr = input("What year you graduated? ")
    Voc = input("Name of your vocational school: ")
    degr = input("What degree you received? ")
    yeaR = input("What year you graduated? ")
    spSkills = input("Enter your skills: ")
    companyN = input("Enter the company name: ")
    yOCCU = input("Your occupation in that company: ")
    salary = input("Your salary range: ")
    Cname = input("Enter the name of your character reference: ")
    Coccu = input("What is her/his occupation? ")
    Cadd = input("What is her/his address? ")
    Ctel = input("His/her telephone number: ")
    cName = input("Enter the name of your character reference: ")
    cOccu = input("What is her/his occupation? ")
    cAdd = input("What is her/his address? ")
    cTel = input("His/her telephone number: ")

    print ("\033[1m--------------------------------------------------------BIO-DATA-------------------------------------------------------------\033[0m " +
    "\n|		    			              \33[4mPERSONAL DATA\33[m	    		    	                            \n" + "| POSITION DESIRED:\33[4m " + positionDs + "\33[m                                                                DATE: \33[4m" + date + "\33[m                      \b\n" +
    "| NAME:\33[4m " + yourName + "          \33[m \n" + "| PRESENT ADDRESS:\33[4m " + presentAdd + "\33[m                         MOBILE NO: \33[4m " + mobileNo + "\33[m                     \n" +
    "| PERMANENT ADDRESS:\33[4m " + permanentAdd + "\33[m                                 HOME NO:\33[4m " + homeNo + "\33[m                      \n" +
    "| DATE OF BIRTH:\33[4m " + dateBirth + "\33[m     " + "PLACE OF BIRTH:\33[4m " + placeBirth + "\33[m     " + "CITIZENSHIP:\33[4m " + citizenship + "\33[m        " + "RELIGION:\33[4m " + religion + "\33[m   \n" + 
    "| AGE:\33[4m " + yAge +   "\33[m      " + "SEX:\33[4m " + ySex + "\33[m             " + "CIVIL STATUS:\33[4m "+ civilStat + "\33[m               " + "HEIGHT:\33[4m " + yHeight + "\33[m                " + "WEIGHT:\33[4m " + yWeight + "\33[m   \n" +
    "| NAME OF SPOUSE:\33[4m " + spouseN + "\33[m                                                                                " + "OCCUPATION:\33[4m " + occup + "\33[m     \n" + 
    "| NO. OF CHILDREN:\33[4m " + noChild + "\33[m                     THEIR NAMES AND DATE OF BIRTH:\33[4m " + namesAbirth + "\33[m                       \n" + 
    "| FATHER'S NAME:\33[4m " + fatherN + "\33[m       " + "OCCUPATION:\33[4m " + fOccup + "\33[m          " + "ADDRESS:\33[4m " + fAdd + "\33[m  \n" + 
    "| MOTHER'S NAME:\33[4m " + motherN + "\33[m     " + "OCCUPATION:\33[4m " + mOccup + "\33[m      " + "ADDRESS:\33[4m " + mAdd + "\33[m  \n" + 
    "| LANGUAGES/DIALECTS YOU CAN SPEAK OR WRITE:\33[4m " + language + "\33[m \n" + 
    "| PERSON TO BE NOTIFIED IN CASE OF EMERGENCY:\33[4m " + pEmergency + "\33[m                                      " + "RELATIONSHIP:\33[4m" + relation + "\33[m \n" + 
    "| ADDRESS:\33[4m " + pAdd + "\33[m                               " + "TEL NO:\33[4m " + pTel + "\33[m \n" + 
    "|=================================================\33[4mEDUCATIONAL BACKGROUND\33[m=======================================================\n" + 
    "|               NAME OF SCHOOL                            DEGREE RECEIVED             YEAR GRADUATED\n" +
    "| ELEMENTARY:\33[4m " + elem + "\33[m                      \33[4m" + deg + "\33[m                      \33[4m" + year + "\33[m \n" + 
    "| HIGH SCHOOL:\33[4m " + highscl + "\33[m               \33[4m" + dEg + "\33[m                 \33[4m" + yEar + "\33[m \n" + 
    "| COLLEGE:\33[4m " + collg + "\33[m                     \33[4m" + deG + "\33[m                        \33[4m" + yeAr + "\33[m \n" + 
    "| VOCATIONAL:\33[4m " + Voc + "\33[m                                               \33[4m" + degr + "\33[m                        \33[4m" + yeaR + "\33[m \n" + 
    "| SPECIAL SKILLS:\33[4m " + spSkills + "\33[m \n" + 
    "|===================================================\33[4mEMPLOYMENT HISTORY\33[m=========================================================\n" + 
    "|      NAME OF THE COMPANY                    OCCUPATION                 SALARY \n" + 
    "|             \33[4m" + companyN + "\33[m                                " + "\33[4m" + yOCCU + "\33[m                      " + "\33[4m"+ salary + "\33[m \n" + 
    "| -------------------------             " + "---------------------          " + "-------------\n" + 
    "| -------------------------             " + "---------------------          " + "-------------\n" + 
    "|==================================================\33[4mCHARACTER REFERENCES\33[m========================================================\n" + 
    "|           NAME                  OCCUPATION                        ADDRESS                                         TEL NO.\n" + ""
    "|    " + "\33[4m " + Cname + "\33[m              \33[4m" + Coccu + "\33[m       \33[4m" + Cadd + "\33[m    " + "\33[4m " + Ctel + "\33[m \n" +
    "|    " + "\33[4m " + cName + "\33[m              \33[4m" + cOccu + "\33[m       \33[4m" + cAdd + "\33[m    " + "\33[4m " + cTel + "\33[m \n")

def activity4():
    number1 = eval(input("Please input a number-->"))
    number2 = eval(input("Please input a number-->"))

    answer = number1 + number2

    print("The sum of" ,number1, "+" ,number2, "is",answer)

def activity5():
    print ("========FAHRENHEIT TO CELSIUS CONVERTER PROGRAM========")
    print ("=======================================================")

    FahrenH = eval(input("Kindly enter the temperature in Fahreinheit --> :   "))
    celsius = ((FahrenH - 32 ) * 5) / 9

    print (f" {FahrenH} degrees Fahrenheit converted to celsius is{round(celsius,2)} degrees")
    print(round(celsius, 2))

def activity6():
    #purpose of the assisgnment operators
    #problem (code scenario)
    #assignment operators are meant to update the value of a variable

    x = 5

    print(x)

    x = x + 10

    print(x)

    x = x + 15

    print(x)

    x += 10

    print(x)

def activity7():
    #introduction to conditional statement

    gold = 0 
    miner = input("Hi good day! What is your name?  ---> ")

    isGold = input("is the mineral gold? ---> ")

    if isGold.lower()== "yes" :
        gold += 1
        print(f"Hi good day! {miner} , Your total number of gold is {gold}")
    else:
        print(f"Hi good day! {miner} , Your total number of gold is {gold}")

def activity8():
    password = input("Enter your password ---> : ")

    if password.lower() == "annyeong":
        print("Access Granted")
        print("We hope you to enjoy using this system!")
    elif password.lower() == "gomawo":
        print("Successfully entered!")
        print("You may now enjoy our system!")
    else:
        print("Oh no! Access denied")
    print("System exit, thank you for using this system")

def activity9():
    age = eval(input("Enter your age ---> : "))

    if age <= 7:
        print(" - Toddler")
    elif age <= 8 and age >= 13:
        print(" - Pre teen")
    elif age <= 14 and age >= 18:
        print(" - Teenage")
    elif age <= 19 and age >= 31:
        print(" - Early adulthood")
    elif age <= 32 and age >= 45:
        print(" - Mid adulthood")
    elif age <= 46 and age >= 59:
        print(" - Past adulthood")
    elif age >= 60:
        print(" - Senior")

    else:
        print("Invalid input")

def activity10():
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

def activity11():
    sum = 1
    for x in range(1, 11):
        number = int(input(f"Enter {x} ------> "))
        sum += number

        print(f"The sum of all numbers given is {sum}")

def activity12():
    odd = 0
    even = 0
    sum = 0

    for c in range(10):
        c = eval(input(f"Enter a number {c+1} : "))
        if c:
            even += c
        else:
            odd += c
            sum += c

    print(f"The sum of all number is:{sum} ")
    print(f"The sum of all EVEN number is:{even} ")
    print(f"The sum of all ODD number is:{odd} ")

def activity13():
    num = eval(input(f"Enter a number: "))
    factorial = 1

    for x in range(num, 0, -1):
        factorial *= x
    print(f"The factorial of {num} is {factorial}")

def activity14():
    #range from 0 to 11
    for x in range(0, 11):
        print(x, end = " ")
        for y in range(0, 11):
            print("*" , end = " ")
        print()

def activity15():
    for x in range(0, 11):
        print(x, end = " ")
        for y in range(0, x):
            print("*" , end = " ")
        print()

def activity16():
    for x in range(1, 11):
        for y in range(11, x, -1):
            print("*" , end = " ")
        print()

        for z in range(1, x+1):
            print(" " , end = " ")

def activity17():
    for x in range(1, 6):
        for y in range(1, x+1):
            print(" " , end = " ")

        for z in range(6, x, -1):
            print("=" , end = " ")

        for a in range(6, x, -1):
            print("#" , end = " ")
    print()

def activity18():
    nt = eval(input("Enter number of triangles: "))
    for x in range(1,5):
        for r in range(1, nt+1):
            for y in range(1, x+1):
                print("*", end=" ")
            for z in range(5, x, -1):
                print(" ", end=" ")
            print(end=" ")
        print()

def activity19():
    isContinue = True 

    while isContinue == True:
        name = input("Give me a name ---> ")

        if name.lower() == "stop":
            print("Loop Terminated")
            break
            isContinue == False 
        else:
            print(f"Hi, {name}")
        continue

def activity20():
    isContinue = True 
    nt = 0
    while isContinue == True:
        ask = input("Do you want to create another triangle? (oo/hindi)")

        if ask.lower() == "stop":
            print("Program terminated")
            break
            isContinue == False 
    
        else:
            nt += 1
            for a in range(1,6):
                for d in range(1,nt+1):
                    for b in range(1,a+1):
                        print("*",end=" ")
                    for c in range(6,a,-1):
                        print(" ",end=" ")
                    print(end=" ")
                print()
            continue

def code_challenge1():
    print ("                      *\n                    * * *\n                  * * * * *\n                 * * * * * *\n                  * * * * *\n                    * * *\n                      *\n")

def code_challenge2():
    name = input("What is your name?-->  ")

    print ("                       *\n                    *  *  *\n                 *  *  *  *  *\n              * Hi, " + name + "       *\n                 *  *  *  *  *\n                    *  *  *\n                       *\n")

def code_challenge3():
    pass

def code_challenge4():
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("Enter another number: "))
    sum = number1 + number2
    subs = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    exponent = number1 ** number2
    remain = number1 % number2
    floorDiv = number1 // number2

    print("The sum of" , number1 , "and" , number2 , "is" , sum , )
    print("The difference of" , number1 , "and" , number2 , "is" , subs , )
    print("The product of" , number1 , "and" , number2 , "is" , product , )
    print("The quotient of" , number1 , "and" , number2 , "is" , quotient , )
    print( number1 , "exponent by" , number2 , "is" , exponent , )
    print("The remainder of" , number1 , "and" , number2 , "is", remain , )
    print("The floor division of" , number1 , "and" , number2 , "is" , floorDiv , )
def code_challenge5():
    print ("========FAHRENHEIT TO CELSIUS CONVERTER PROGRAM========")
    print ("=======================================================")

    FahrenH = eval(input("Kindly enter the temperature in Fahreinheit --> :   "))
    celsius = ((FahrenH - 32 ) * 5) / 9

    print (f" {FahrenH} degrees Fahrenheit converted to celsius is{round(celsius,2)} degrees")
    print(round(celsius, 2))

def code_challenge6():
    pass

def code_challenge7():
    def grocery_purchase():
    #Questions
        purchase = input("Did you buy a grocery? Yes/No:   ").stip().lower()
        if purchase != "Yes":
            print("Thank you for trusting")
        return
    item = input("Name of the item:   ")
    price = float(input("Price of the item:   "))
    age = eval(input("Age: "))
    amount = float(input("Amount given:  "))
    #Discount
    discount = 0
    if age >= 60:
        discount = price * 0.052 #5.2 discount
    #Tax
    Tax = price * 0.123
    #Calculate total price
    Totalamount = price + Tax
    #If had discount
    discounted = price + Tax - discount
    #Calculate the change
    change = amount - discounted

    #THE OUTPUT
    print(f"Hi customer, you purchased a {item} , with a price of {price:.2f} plus 12.3% tax ({Tax:.2f}) with the total amount of ")
    print(f"Total of {Totalamount}.")
    print(f"Amount given: {amount}")
    print(f"Discounted price: {discounted}")
    print(f"Change: {change}")

def code_challenge8():
    odd = 0
    even = 0
    sum = 0 
    for i in range(10):
        i = eval(input(f"Enter a number {i+1}: "))
        if i %2 == 0:
            even += i
        else:
            odd += i
        sum += i
    print(f"The sum of all Even number is: {even} ")
    print(f"The sum of all Odd number is: {odd} ")
    print(f"The sum of all number is: {sum} ")

def code_challenge9():
    for x in range(0, 11):
        print(x, end = " ")
        for y in range(x, 11):
            print("*", end=" ")
        print()

def code_challenge10():
        
    for  x in range(1,7):
        for y in range(7, x, -1):
            print(" ", end = " ")

        for z in range(1, x+1):
            print("<", end = " ")

        for a in range(1, x+1):
            print(">", end= " ")
        print()

    for  x in range(1,7):
        for y in range(1, x + 1):
            print(" ", end = " ")

        for z in range(7, x, -1):
            print("(", end = " ")

        for a in range(7, x, -1):
            print(")", end= " ")
        print()

def code_challenge11():
    for  x in range(1,7):
        for y in range(7, x, -1):
            print(" ", end = " ")

        for z in range(1, x+1):
            print("*", end = " ")

        for a in range(2, x+1):
            print("*", end= " ")
        print()

    for  x in range(1,7):
        for y in range(0, x + 1):
            print(" ", end = " ")

        for z in range(5, x, -1):
            print("*", end = " ")

        for a in range(6, x, -1):
            print("*", end= " ")
        print()

def code_challenge12():
    for  x in range(8,1,-1):
        for z in range(x,0, -1):
            print(" ", end = " ")

        for y in range(7, x, -1):
            print("*", end = " ")

        for a in range(7, x, -1):
            print("*", end= " ")
        print()

    for  x in range(5,0,-1):
        for z in range(6,0,-1):
            print(" ", end = " ")
    
        for y in range(1,2):
            print("*", end = " ")

        for a in range(1,2):
            print("*", end= " ")
        print()

def code_challenge13():
    print()

    for  a in range(1,6):
        for b in range(6,a, -1):
            print(" ", end = " ")

        for c in range(a,1,-1):
            print(c, end = " ")

        for d in range(1, a+1):
            print(d, end= " ")
        print()

    for  a in range(4,0,-1):
        for b in range(6,a,-1):
            print(" ", end = " ")

        for c in range(a,1, -1):
            print(c, end = " ")

        for d in range(1,a+1):
            print(d, end= " ")
        print()
    print()

def code_challenge14():
    total_sum = 0 

    #continue to ask user for a number
    while True:
        try:
            #Ask the user to enter a number
            user = int(input("Enter a number ---->   "))
            #Add the number for total sum
            total_sum += user

        except ValueError:
            #If the users enters an invalid number like string, stop the loop
            print("Please enter a valid number")
            break
    #Output
    print("Loop has terminated")
    print("The sum of all the numbers given is:", total_sum)

def code_challenge15():
    tuloy_lang = True
    number = 0 
    while tuloy_lang:
        itanong = input("Do you wish to create a new triangle (Yes/No) ---->  ")

        if itanong.lower() == "no":
            print("program / loop terminated")
            break
        elif itanong.lower() == "yes":
            number += 1
            for x in range(1,6):
                for t in range(1, number + 1):
                    for a in range(1, x+1):
                        print(a, end = " ")
                    for b in range(6, x, -1):
                        print(" ", end = " ")
                print()
        continue
    else:
        print("Invalid response, please input only 'yes' or 'no'")

def code_challenge16():
    class BankAccount:
        def __init__(me, your_name, initial_deposit):
            me.name = your_name
            me.balance = initial_deposit

        def deposit(me, amount):
            me.balance += amount
            print(f"Deposited {amount}. Balance: {me.balance}")
            me.breakdown_denomination(amount)

        def withdraw(me, amount):
            if amount > me.balance:
                print("Insufficient funds.")
            else:
                me.balance -= amount
                print(f"Withdrew {amount}. Balance: {me.balance}")

        def check_balance(me):
            print(f"Balance: {me.balance}")

        def breakdown_denomination(me, amount):
            denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
            print("Denomination breakdown:")
            for denom in denominations:
                count = amount // denom
                if count > 0:
                    print(f"{denom} peso: {count} bill(s)")
                    amount -= count * denom

    def create_account():
        your_name = input("Name: ")
        while True:
            try:
                deposit = float(input("Initial deposit: "))
                return BankAccount(your_name, deposit)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit.")

    def main():
        account = None
        while True:
            print("\n1. Create account\n2. Deposit\n3. Withdraw\n4. Balance\n5. Exit")
            choice = input("Choice: ")

            if choice == "1" and not account:
                account = create_account()
            elif choice == "2" and account:
                while True:
                    try:
                        amount = float(input("Deposit amount: "))
                        account.deposit(amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the deposit amount.")
            elif choice == "3" and account:
                while True:
                    try:
                        amount = float(input("Withdraw amount: "))
                        account.withdraw(amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the withdrawal amount.")
            elif choice == "4" and account:
                account.check_balance()
            elif choice == "5":
                print("That's all, thank you!")
                break
            else:
                print("Invalid choice or account not created.")

    if __name__ == "__main__":
        main()

while isContinue:
    print("\nSelect from the following code")
    print("Activities: ")
    print("1 - Hello world")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")
    print("8")
    print("9")
    print("10")
    print("11")
    print("12")
    print("13")
    print("14")
    print("15")
    print("16")
    print("17")
    print("18")
    print("19")
    print("20")
    print("\nCODE CHALLENGES\nUse cc for selecting (ex: cc1)")
    print("Code Challenge 1")
    print("Code Challenge 2")
    print("Code Challenge 3")
    print("Code Challenge 4")
    print("Code Challenge 5")
    print("Code Challenge 6")
    print("Code Challenge 7")
    print("Code Challenge 8")
    print("Code Challenge 9")
    print("Code Challenge 10")
    print("Code Challenge 11")
    print("Code Challenge 12")
    print("Code Challenge 13")
    print("Code Challenge 14")
    print("Code Challenge 15")
    print("Code Challenge 16")

    print("100 - EXIT")
    ask = input("\nWhich program would you like to run, select options from above: ")

    if ask == "1":
        print("ACTIVITY 1\n")
        activity1()
        continue

    if ask == "2":
        print("ACTIVITY 2\n")
        activity2()
        continue

    if ask == "3":
        print("ACTIVITY 3\n")
        activity3()
        continue
    
    if ask == "4":
        print("ACTIVITY 4\n")
        activity4()
        continue

    if ask == "5":
        print("ACTIVITY 5\n")
        activity5()
        continue

    if ask == "6":
        print("ACTIVITY 6\n")
        activity6()
        continue

    if ask == "7":
        print("ACTIVITY 7\n")
        activity7()
        continue

    if ask == "8":
        print("ACTIVITY 8\n")
        activity8()
        continue

    if ask == "9":
        print("ACTIVITY 9\n")
        activity9()
        continue
    
    if ask == "10":
        print("ACTIVITY 10\n")
        activity10()
        continue
    
    if ask == "11":
        print("ACTIVITY 11\n")
        activity11()
        continue

    if ask == "12":
        print("ACTIVITY 12\n")
        activity12()
        continue

    if ask == "13":
        print("ACTIVITY 13\n")
        activity13()
        continue
    
    if ask == "14":
        print("ACTIVITY 14\n")
        activity14()
        continue
    
    if ask == "15":
        print("ACTIVITY 15\n")
        activity15()
        continue
    
    if ask == "16":
        print("ACTIVITY 16\n")
        activity16()
        continue
    
    if ask == "17":
        print("ACTIVITY 17\n")
        activity17()
        continue
    
    if ask == "18":
        print("ACTIVITY 18\n")
        activity18()
        continue
    
    if ask == "19":
        print("ACTIVITY 19\n")
        activity19()
        continue
    
    if ask == "20":
        print("ACTIVITY 20\n")
        activity20()
        continue

    if ask == "cc1":
        print("Code Challenge 1")
        code_challenge1()
        continue

    if ask == "cc2":
        print("Code Challenge 2")
        code_challenge2()
        continue

    if ask == "cc3":
        print("Code Challenge 3")
        code_challenge3()
        continue

    if ask == "cc4":
        print("Code Challenge 4")
        code_challenge4()
        continue

    if ask == "cc5":
        print("Code Challenge 5")
        code_challenge5()
        continue

    if ask == "cc6":
        print("Code Challenge 6")
        code_challenge6()
        continue

    if ask == "cc7":
        print("Code Challenge 7")
        continue

    if ask == "cc8":
        print("Code Challenge 8 ")
        code_challenge8()
        continue

    if ask == "cc9":
        print("Code Challenge 9")
        code_challenge9()
        continue

    if ask == "cc10":
        print("Code Challenge 10")
        code_challenge10()
        continue

    if ask == "cc11":
        print("Code Challenge 11")
        code_challenge11()
        continue

    if ask == "cc12":
        print("Code Challenge 12")
        code_challenge12()
        continue
    
    if ask == "cc13":
        print("Code Challenge 13")
        code_challenge13()
        continue

    if ask == "cc14":
        print("Code Challenge 14")
        code_challenge14()
        continue

    if ask == "cc15":
        print("Code Challenge 15")
        code_challenge15()
        continue

    if ask == "cc16":
        print("Code Challenge 16")
        code_challenge1()
        continue

    if ask.lower() == "100":
        print("Program terminated")
        break

    else:
        print("Invalid Choice, Please try again. ")
        continue