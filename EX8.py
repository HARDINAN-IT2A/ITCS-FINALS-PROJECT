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