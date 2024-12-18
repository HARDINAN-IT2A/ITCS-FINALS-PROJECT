print("""
        Definition of Conditional Statement:
        
        Conditional statements in Python allow you to execute
        specific blocks of code based on whether a condition is true or false. 
        These statements are fundamental for controlling the flow of a program 
        and making decisions within the code.
          
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