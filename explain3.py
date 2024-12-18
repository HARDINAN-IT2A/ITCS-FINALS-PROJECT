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