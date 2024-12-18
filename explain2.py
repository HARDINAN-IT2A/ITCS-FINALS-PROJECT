print("""
INPUT:
     
    number1 = eval(input("Please input a number-->"))
    number2 = eval(input("Please input a number-->"))

    answer = number1 + number2

    print("The sum of" ,number1, "+" ,number2, "is",answer)
     

EXPLANATION:
     
      ------    number1   and     number2    -------
    1. Both are the variables 
     
    ------   number1 = eval(input("Please input a number-->"))   -------
    1. input() prompts the user to enter a value.
    2. eval() evaluates the input as a Python expression.
    So, if the user enters "5", it will be treated as the integer 5.
     
    ------    answer = number1 + number2   ------
    1.  Adds the two numbers (input by the user) 
    -----   print("The sum of" ,number1, "+" ,number2, "is",answer)   ------
    1. Will prints the sum of number1 and number2
""")