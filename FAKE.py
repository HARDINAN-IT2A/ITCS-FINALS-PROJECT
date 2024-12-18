def menu1():
    print("""
    =====================SUBMENU====================
                    PRINT STATEMENTS
              
        1. Simple printing
        2. Printing with escape sequence
        0. Exit
              
    ================================================
    """)

def menu2():
    print("""
    =====================SUBMENU====================
                        VARIABLES
              
        1. Basic addition of numbers
        2. Printing with escape sequence
        0. Exit
              
    ================================================
    """)

def menu3():
    print("""
    =====================SUBMENU====================
                        OPERATORS
              
        1. Basic Arithmetic Operators
        0. Exit
              
    ================================================
    """)

def menu4():
    print("""
    =====================SUBMENU====================
                        CONDITIONAL STATEMENTS
              
        1. If statement
        2. If-else statement
        0. Exit
              
    ================================================
    """)

def menu5():
    print("""
    =====================SUBMENU====================
                        LOOP STATEMENTS
              
        1. For loop
        2. While loop
        0. Exit
              
    ================================================
    """)

def menu6():
    print("""
    =====================SUBMENU====================
                        LISTS
              
        1. Creating a list
        2. Accessing elements in a list
        0. Exit
              
    ================================================
    """)

def menu7():
    print("""
    =====================SUBMENU====================
                        FUNCTIONS
              
        1. Defining a function
        2. Calling a function
        0. Exit
              
    ================================================
    """)

# Main Program Loop
TULOY = True
while TULOY:
    askName = input("Annyeonhaseyo! What is your name? ")
    itanong = input("\nDo you wish to open a program? (Yes/No) ---->  ")
    if itanong.lower() == "no":
        print("Program / loop terminated. Thank you for using my system.")
        break
    elif itanong.lower() == "yes":

        print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON MAIN MENU
              
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

    # MAIN MENU
    while True:  # Loop for returning to the main menu
        ask = input("\nWhich program would you like to run, select options from above: ")

        if ask == "1":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu1()
            while True:  # Print Statements submenu
                ask_subMenu = input("\nWhich topic from PRINT STATEMENTS would you like to learn? Please select options from above: ")

                if ask_subMenu == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the SIMPLE PRINTING""")
                    Example1()
                elif ask_subMenu == "2":
                    print(f"""\nAnnyeong! {askName} , Welcome to the PRINTING WITH ESCAPE SEQUENCE""")
                    defin2()
                    Sample2()
                elif ask_subMenu == "0":
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "2":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu2()
            while True:  # Variables submenu
                ask_subMenu2 = input("\nWhich topic from VARIABLES would you like to learn? Please select options from above: ")

                if ask_subMenu2 == "1":
                    print(f"""\nAnnyeong! {askName} , Welcome to the VARIABLES of Python""")
                    Addition()  # Addition task
                elif ask_subMenu2 == "0":
                    print(f"\nReturning to the main menu...\n")  # Message before returning
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "3":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu3()
            while True:  # Operators submenu
                ask_subMenu3 = input("\nWhich topic from OPERATORS would you like to learn? Please select options from above: ")

                if ask_subMenu3 == "1":
                    print("Basic Arithmetic Operators example")  # Add the operator examples here
                elif ask_subMenu3 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "4":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu4()
            while True:  # Conditional statements submenu
                ask_subMenu4 = input("\nWhich topic from CONDITIONAL STATEMENTS would you like to learn? Please select options from above: ")

                if ask_subMenu4 == "1":
                    print("If statement example")  # Add the if statement example here
                elif ask_subMenu4 == "2":
                    print("If-else statement example")  # Add the if-else statement example here
                elif ask_subMenu4 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "5":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu5()
            while True:  # Loop statements submenu
                ask_subMenu5 = input("\nWhich topic from LOOP STATEMENTS would you like to learn? Please select options from above: ")

                if ask_subMenu5 == "1":
                    print("For loop example")  # Add the for loop example here
                elif ask_subMenu5 == "2":
                    print("While loop example")  # Add the while loop example here
                elif ask_subMenu5 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "6":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu6()
            while True:  # Lists submenu
                ask_subMenu6 = input("\nWhich topic from LISTS would you like to learn? Please select options from above: ")

                if ask_subMenu6 == "1":
                    print("Creating a list example")  # Add the list creation example here
                elif ask_subMenu6 == "2":
                    print("Accessing elements in a list")  # Add list element access example here
                elif ask_subMenu6 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "7":
            print(f"""\nAnnyeong! {askName} , Welcome to the PYTHON SUBMENU""")
            menu7()
            while True:  # Functions submenu
                ask_subMenu7 = input("\nWhich topic from FUNCTIONS would you like to learn? Please select options from above: ")

                if ask_subMenu7 == "1":
                    print("Defining a function example")  # Add the function definition example here
                elif ask_subMenu7 == "2":
                    print("Calling a function example")  # Add the function calling example here
                elif ask_subMenu7 == "0":
                    print(f"\nReturning to the main menu...\n")
                    break  # Exit to the main menu
                else:
                    print("Invalid choice, please try again.")
        
        elif ask == "8":
            print(f"""\nAnnyeong! {askName} , Goodbye!""")
            break  # Exit the program
        
        else:
            print("Invalid choice, please try again.")  # Keep the submenu active until a valid input is given
