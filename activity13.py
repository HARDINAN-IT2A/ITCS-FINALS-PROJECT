num = eval(input(f"Enter a number: "))
factorial = 1

for x in range(num, 0, -1):
    factorial *= x
print(f"The factorial of {num} is {factorial}")