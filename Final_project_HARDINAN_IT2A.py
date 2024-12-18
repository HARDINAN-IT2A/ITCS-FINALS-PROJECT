def Example1():
    print(""""
        
        GIVEN PROGRAM:
            
        INPUT:         
                    print("Annyeong , welcome to programming!")

        OUTPUT: 
                    Annyeong , welcome to programming!

        Definition:
                    print() - prints the message
                    "" - used for String/sentences/phrases   
                      """)
def menu1():
    print("""
    =====================SUBMENU====================
                    PRINT STATEMENTS
              
        1. Simple printing
        2. Printing with escape sequence
        0. Exit 
    ================================================
    """)

def explain():
    print("""
    Python print() function prints the message to
    the screen or any other standard output device.\n""")

def defin2():
    print("""
        To add a newline in Python, you can use the escape sequence.
        This is the most common and straightforward way to insert a newline character in your strings.
        """)
def Sample2():
    print("""
          
        GIVE PROGRAM:
        
          INPUT:

                print("                      *\ n                    * * *\ n                  * * * * *\ n                 * * * * * *\ n                  * * * * *\ n                    * * *\ n                      *\ n")
          
          
          OUTPUT:

                      *
                    * * *
                  * * * * *
                 * * * * * *
                  * * * * *
                    * * *
                      *
      """)
    
def menu2():
    print("""
    =====================SUBMENU====================
                        VARIABLES
              
        1. Definition & Example
        2. Addition of variables (A code program)
        0. Exit
    ================================================
    """)

def EX1():
    print("""
          
        Definition of Variables:
          Python languages, Python is dynamically typed, meaning
          you do not need to declare a variable's type before using it.
          A variable is created the moment you first assign a value to it

        EXAMPLE 1: 

        INPUT:  
    
            num1 = 10
            num2 = 20

            sum_result = num1 + num2

            print("The sum of", num1, "and", num2, "is", sum_result)
      
        OUTPUT:
            The sum of 10 and 20 is 30
          
        GIVEN PROGRAM YOU CAN USE:
      
        number1 = eval(input("Please input a number-->"))
        number2 = eval(input("Please input a number-->"))

        answer = number1 + number2

        print("The sum of" ,number1, "+" ,number2, "is",answer)
        """)
    
def Addition():
    number1 = eval(input("Please input a number-->"))
    number2 = eval(input("Please input a number-->"))

    answer = number1 + number2

    print("The sum of" ,number1, "+" ,number2, "is",answer)


def menu3():
    print("""
        =====================SUBMENU====================
                            OPERATORS
              
            1. Definition & Example
            2. Arithmetic OperatorS (A code program)
            3. Comparison Operators (A code program)
            0. Exit
        ================================================
        """)

def explain3():
    print(""""
      Definition of Arithmetic & comparison operators:

      Arithmetic operators in Python are used to perform
      common mathematical operations on numeric values. 
      These operators include addition, subtraction, multiplication,
      division, modulus, exponentiation, & floor division
      While comparison operators was use to compare two variables if
      it is equal, not equal etc...
    
    EXAMPLE 1:

    INPUT:

            # Input two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            #Arithmetic operations
            sum_result = num1 + num2
            difference = num1 - num2
            product = num1 * num2
            quotient = num1 / num2 if num2 != 0 else "undefined"  # Handling division by zero

            # Comparison operations
            is_equal = num1 == num2
            is_not_equal = num1 != num2
            is_greater = num1 > num2
            is_less = num1 < num2
            is_greater_equal = num1 >= num2
            is_less_equal = num1 <= num2

            #Display results
            print("\nArithmetic Results:")
            print(f"The sum of {num1} and {num2} is {sum_result}")
            print(f"The difference of {num1} and {num2} is {difference}")
            print(f"The product of {num1} and {num2} is {product}")
            print(f"The quotient of {num1} and {num2} is {quotient}")

            print("\nComparison Results:")
            print(f"Are {num1} and {num2} equal? {is_equal}")
            print(f"Are {num1} and {num2} not equal? {is_not_equal}")
            print(f"Is {num1} greater than {num2}? {is_greater}")
            print(f"Is {num1} less than {num2}? {is_less}")
            print(f"Is {num1} greater than or equal to {num2}? {is_greater_equal}")
            print(f"Is {num1} less than or equal to {num2}? {is_less_equal}")
          
    OUTPUT:
            Enter the first number: 5
            Enter the second number: 20

            Arithmetic Results:
            The sum of 5.0 and 20.0 is 25.0        
            The difference of 5.0 and 20.0 is -15.0
            The product of 5.0 and 20.0 is 100.0   
            The quotient of 5.0 and 20.0 is 0.25   

            Comparison Results:
            Are 5.0 and 20.0 equal? False
            Are 5.0 and 20.0 not equal? True       
            Is 5.0 greater than 20.0? False
            Is 5.0 less than 20.0? True
            Is 5.0 greater than or equal to 20.0? False
            Is 5.0 less than or equal to 20.0? True
          
    GIVEN PROGRAM YOU CAN USE 1:

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
          
    GIVEN PROGRAM YOU CAN USE 2:
          
            #Input two numbers
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))

            #Using comparison operators
            print(f"{number1} > {number2}: {number1 > number2}") #Greater than
            print(f"{number1} < {number2}: {number1 < number2}") #Less than
            print(f"{number1} == {number2}: {number1 == number2}") #Equal to
            print(f"{number1} != {number2}: {number1 != number2}") #Not equal to
            print(f"{number1} >= {number2}: {number1 >= number2}") #Greater than or equal to
            print(f"{number1} <= {number2}: {number1 <= number2}") #Less than or equal to
        """)

def Operators():
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

def Operators2():
    #Input two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    #Using comparison operators
    print(f"{number1} > {number2}: {number1 > number2}") #Greater than
    print(f"{number1} < {number2}: {number1 < number2}") #Less than
    print(f"{number1} == {number2}: {number1 == number2}") #Equal to
    print(f"{number1} != {number2}: {number1 != number2}") #Not equal to
    print(f"{number1} >= {number2}: {number1 >= number2}") #Greater than or equal to
    print(f"{number1} <= {number2}: {number1 <= number2}") #Less than or equal to

def menu4():
    print("""
    =====================SUBMENU====================
                CONDITIONAL STATEMENTS
              
        1. Definition & Example
        2. Using if, elif & else statement (A code program)
        0. Exit
    ================================================
    """)
    
def  Explain4():
    print("""
        Definition of Conditional Statement:
        
        Conditional statements in Python allow you to execute
        specific blocks of code based on whether a condition is true or false. 
        These statements are fundamental for controlling the flow of a program 
        and making decisions within the code.

    EXAMPLE 1:

    INPUT:
    
        password = input("Enter your password ---> : ")

        if password.lower() == "iloveyou123":
            print("Access Granted")
            print("We hope you to enjoy using this system!")
        elif password.lower() == "labyutoo":
            print("Successfully entered!")
            print("You may now enjoy our system!")
        else:
            print("Oh no! Access denied")
        print("System exit, thank you for using this system")
      
    OUTPUT:
        #if the user input correct password
      
        Enter your password ---> : iloveyou123
        Access Granted
        We hope you to enjoy using this system!     
        System exit, thank you for using this system
      
        #if the user input another correct password
      
        Enter your password ---> : labyutoo
        Succesfully entered!
        You may now enjoy our system!     
        System exit, thank you for using this system
      
        #if the user input wrong password
      
        Enter your password ---> : mahalkita
        Oh no! Access denied
        System exit, thank you for using this system
          
    GIVEN PROGRAM YOU CAN USE:
          
        age = eval(input("Enter your age ---> : "))

        if age <= 7:
            print(" - Toddler")
        elif age >= 8 and age <= 13:
            print(" - Pre teen")
        elif age >= 14 and age <= 18:
            print(" - Teenage")
        elif age >= 19 and age <= 31:
            print(" - Early adulthood")
        elif age >= 32 and age <= 45:
            print(" - Mid adulthood")
        elif age >= 46 and age <= 59:
            print(" - Past adulthood")
        elif age >= 60:
            print(" - Senior")
        else:
            print("Invalid input")
        """)
    
def condiStat():
    age = eval(input("Enter your age ---> : "))

    if age <= 7:
        print(" - Toddler")
    elif age >= 8 and age <= 13:
        print(" - Pre teen")
    elif age >= 14 and age <= 18:
        print(" - Teenage")
    elif age >= 19 and age <= 31:
        print(" - Early adulthood")
    elif age >= 32 and age <= 45:
        print(" - Mid adulthood")
    elif age >= 46 and age <= 59:
        print(" - Past adulthood")
    elif age >= 60:
        print(" - Senior")
    else:
        print("Invalid input")

def menu5():
    print("""
    =====================SUBMENU====================
                    LOOPING STATEMENTS
              
        1. Definition & Example
        2. Using if, elif & else statement (A code program)
        3. Nested loop (A code program)
        0. Exit
    ================================================
    """)
def EX5():
    print("""
      Definition of while and for loop & Nested loop:
        A while loop is used to execute a block of statements repeatedly
        until a given condition is satisfied. When the condition becomes false,
        the line immediately after the loop in the program is executed.
      
        For loops are used for sequential traversal. For example:
        traversing a list or string or array etc. In Python, there
        is “for in” loop which is similar to foreach loop in other
        languages.
          
        In Python, a nested loop is a loop inside another loop.
        This structure is useful for iterating over multi-dimensional
        data structures, such as lists of lists, or for performing tasks
        that require multiple levels of looping. The inner loop will be
        executed one time for each iteration of the outer loop
      
        Note: The continue statement in Python returns the control to the beginning of the loop.
    
    EXAMPLE 1:

    INPUT:
      
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
      
    OUTPUT:
        Give me a name ---> Sunjae
        Hi, Sunjae
        Give me a name ---> Chris
        Hi, Chris
        Give me a name ---> stop
        Loop Terminated
          
    GIVEN PROGRAM YOU CAN USE FOR WHILE LOOP AND FOR LOOP:
          
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
          
    GIVEN PROGRAM YOU CAN USE FOR NESTED CONDITION:
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
            print("Thank you for using the system!")
      """)
    
def Loops():
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

def nested():
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
        print("Thank you for using the system!")

def menu6():
    print("""
    =====================SUBMENU====================
                    LISTS IN PYTHON
              
        1. Definition & Example
        2. Lists and list Operations (A code program output)
        0. Exit
    ================================================
    """)

def Explain6():
    print(""""
        Definition of lists:

        Lists are a fundamental data structure in Python used to store collections of items.
        They are versatile, allowing you to store multiple items in a single variable.
        Lists are created using square brackets [] and can contain items of different data types,
        including integers, strings, and even other lists
    
    EXAMPLE:     

    INPUT:
      
            # List of fruits
            fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

            #Print the list of fruits
            print(f"List of fruits: {fruits}")

            #print the second fruit
            print(f"The second fruit in the list is: {fruits[1]}")

            #Adding a new fruit to the list
            fruits.append("Fig")
            print(f"Updated list of fruits: {fruits}")
      
    OUTPUT:
      
            List of fruits: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
            The second fruit in the list is: Banana
            Updated list of fruits: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig']
          
    GIVEN PROGRAM YOU CAN USE:
          
            #List of countries
            Asian_countries = ["Philippines" , "China" , "Japan" , "Taiwan" , "Malaysia"  , "South Korea"]

            print("List of countries:", Asian_countries)

            print("\nThe first country in the list is:", Asian_countries[0])  #First country in the list
            print("The last country in the list is:", Asian_countries[-1]) #Last country in the list

            #Adding a new country to the list
            Asian_countries.append("Singapore")
            print("\nLatest List of countries after adding South Korea:", Asian_countries)

            #Removing a country from the list
            Asian_countries.remove("China")
            print("\nList of countries after removing China:", Asian_countries)

            #Sorting the list of countries
            Asian_countries.sort()
            print("\nSorted List of countries:", Asian_countries)

            #Length of the list (how many countries in the list)
            print("\nNumber of countries in the list:", len(Asian_countries))

            #Checking if a country is in the list
            check_country = "Philippines"
            if check_country in Asian_countries:
                print(f"\n{check_country} is in the list.")
            else:
                print(f"\n{check_country} is not in the list.")
        """)

def Lists():
    #List of countries
    Asian_countries = ["Philippines" , "China" , "Japan" , "Taiwan" , "Malaysia"  , "South Korea"]

    print("List of countries:", Asian_countries)

    print("\nThe first country in the list is:", Asian_countries[0])  #First country in the list
    print("The last country in the list is:", Asian_countries[-1]) #Last country in the list

    #Adding a new country to the list
    Asian_countries.append("Singapore")
    print("\nLatest List of countries after adding South Korea:", Asian_countries)

    #Removing a country from the list
    Asian_countries.remove("China")
    print("\nList of countries after removing China:", Asian_countries)

    #Sorting the list of countries
    Asian_countries.sort()
    print("\nSorted List of countries:", Asian_countries)

    #Length of the list (how many countries in the list)
    print("\nNumber of countries in the list:", len(Asian_countries))

    #Checking if a country is in the list
    check_country = "Philippines"
    if check_country in Asian_countries:
        print(f"\n{check_country} is in the list.")
    else:
        print(f"\n{check_country} is not in the list.")

def menu7():
    print("""
        =====================SUBMENU====================
                        FUNCTION IN PYTHON
              
            1. Definition & Example
            2. Function (A code program output)
            0. Exit
        ================================================
        """)

def EX8():
    print(""" 
        Definition of Functions:

        A function is a block of code which only runs when it is called.
        You can pass data, known as parameters, into a function.
        A function can return data as a result.  
    
    EXAMPLE:
          
    INPUT:

        def add_numbers(a, b):
        return a + b

        #Example usage
        result = add_numbers(3, 5)
        print(result)  #This should output 8
          
    OUTPUT:
        8
        
    GIVEN PROGRAM YOU CAN USE:

        def add(a, b): 
            return a + b
        def subtract(a, b): 
            return a - b
        def multiply(a, b): 
            return a * b
        def divide(a, b): 
            return a / b if b != 0 else "Error! Division by zero."

        #Main program
        def calculator():
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
    
            operation = input("Enter operation (+, -, *, /): ")
    
            if operation == '+': result = add(num1, num2)
            elif operation == '-': result = subtract(num1, num2)
            elif operation == '*': result = multiply(num1, num2)
            elif operation == '/': result = divide(num1, num2)
            else: result = "Invalid operation"
    
        print("Result:", result)

    calculator()      
          """)
    
def Functions():
    def add(a, b): 
        return a + b
    def subtract(a, b): 
        return a - b
    def multiply(a, b): 
        return a * b
    def divide(a, b): 
        return a / b if b != 0 else "Error! Division by zero."

    #Main program
    def calculator():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        operation = input("Enter operation (+, -, *, /): ")
    
        if operation == '+': result = add(num1, num2)
        elif operation == '-': result = subtract(num1, num2)
        elif operation == '*': result = multiply(num1, num2)
        elif operation == '/': result = divide(num1, num2)
        else: result = "Invalid operation"
    
        print("Result:", result)

    calculator()
    

# Main Program Loop
TULOY = True
while TULOY:
    askName = input("Annyeonghaseyo! What is your name? ")
    itanong = input("\nDo you wish to open a program? (Yes/No) ---->  ")
    if itanong.lower() == "no":
        print("Program / loop terminated. Thank you for using my system.")
        break
    elif itanong.lower() == "yes":

        print(f"\nAnnyeong! {askName} , Welcome to the PYTHON MAIN MENU")

    #MAIN MENU
    while True:  #Loop for returning to the main menu
        print("""
        ===================MAIN MENU===================
              
        1. Print statements in PYTHON
        2. Variables in PYTHON
        3. Operators in PYTHON
        4. Conditional statements in PYTHON
        5. Loop statements in PYTHON
        6. Lists in PYTHON
        7. Functions in PYTHON
        8. Exit
              
        ================================================
        """)
        ask = input("\nWhich program would you like to run, select options from above: ")

        if ask == "1":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu1()
            while True:  #Print Statements submenu
                ask_subMenu = input("\nWhich topic from PRINT STATEMENTS would you like to learn? Please select options from above: ")

                if ask_subMenu == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the SIMPLE PRINTING""")
                    Example1()
                    menu1()
                elif ask_subMenu == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to the PRINTING WITH ESCAPE SEQUENCE""")
                    defin2()
                    Sample2()
                    menu1()
                elif ask_subMenu == "0":
                    break  #Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "2":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu2()
            while True:  #Variables submenu
                ask_subMenu2 = input("\nWhich topic from VARIABLES would you like to learn? Please select options from above: ")

                if ask_subMenu2 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to DEFINITION & EXAMPLE OF VARIABLES""")
                    EX1()  #Addition task
                    menu2()
                    continue
                if ask_subMenu2 == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to the ADDITION OF VARIABLES""")
                    Addition()  #Concatenation task
                    menu2()
                elif ask_subMenu2 == "0":
                    print(f"\nReturning to the main menu...\n")  #Message before returning
                    break  #Exit to the main menu
        
        elif ask == "3":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu3()
            while True:  #Operators submenu
                ask_subMenu3 = input("\nWhich topic from OPERATORS would you like to learn? Please select options from above: ")

                if ask_subMenu3 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the DEFINIITION AND EXAMPLE OF OPERATORS""")
                    explain3()
                    menu3()
                if ask_subMenu3 == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to the ARITHMETIC OPERATORS""")
                    Operators()
                    menu3()
                    continue
                if ask_subMenu3 == "3":
                    print(f"""\nAnnyeong! {askName} , Welcome to the COMPARISON OPERATORS""")
                    Operators2()
                    menu3()
                    continue
                elif ask_subMenu3 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  #Exit to the main menu
        
        elif ask == "4":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu4()
            while True:  #Conditional statements submenu
                ask_subMenu4 = input("\nWhich topic from CONDITIONAL STATEMENTS would you like to learn? Please select options from above: ")

                if ask_subMenu4 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the DEFINITION & EXAMPLE OF CONDITIONAL STATEMENT\n""") #Definition
                    Explain4()
                    menu4()
                elif ask_subMenu4 == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to if, elif & else statement""") #Example4
                    condiStat()
                    menu4()  #if,if-else & else statement example
                elif ask_subMenu4 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  #Exit to the main menu
        
        elif ask == "5":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu5()
            while True:  #Loop statements submenu
                ask_subMenu5 = input("\nWhich topic from LOOP STATEMENTS would you like to learn? Please select options from above: ")

                if ask_subMenu5 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the DEFINITION & EXAMPLE OF LOOPING STATEMENT""")  #looping example
                    EX5()
                    menu5()
                elif ask_subMenu5 == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to for and while LOOPING STATEMENT""")
                    Loops()
                    menu5()
                    continue
                elif ask_subMenu5 == "3":
                    print(f"""\nAnnyeong! {askName} , Welcome to NESTED LOOPING STATEMENT""")
                    nested()
                    menu5()
                    continue
                elif ask_subMenu5 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  #Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "6":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu6()
            while True:  #Lists submenu
                ask_subMenu6 = input("\nWhich topic from LISTS would you like to learn? Please select options from above: ")

                if ask_subMenu6 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the DEFINITION & EXAMPLE OF LISTS""")  #Definition and example
                    Explain6()
                    menu6()
                elif ask_subMenu6 == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to the LISTS & LIST OPERATIONS""")  #A program output of lists
                    Lists()
                    menu6()
                    continue
                elif ask_subMenu6 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  #Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "7":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu7()
            while True:  #Functions submenu
                ask_subMenu7 = input("\nWhich topic from FUNCTIONS would you like to learn? Please select options from above: ")

                if ask_subMenu7 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the DEFINITION & EXAMPLE OF FUNCTION""")
                    EX8()
                    menu7()
                elif ask_subMenu7 == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to the FUNCTIONS OF PYTHON""")
                    Functions()
                    menu7()
                elif ask_subMenu7 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  #Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "8":
            print(f"""\nAnnyeong! {askName} , Goodbye!""")
            break  #Exit the program
        
        else:
            print("Invalid choice, please try again.")  # Keep the submenu active until a valid input is given