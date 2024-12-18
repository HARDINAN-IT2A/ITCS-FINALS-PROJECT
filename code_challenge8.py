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