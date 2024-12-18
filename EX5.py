print("""
      Definition of while and for loop:
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